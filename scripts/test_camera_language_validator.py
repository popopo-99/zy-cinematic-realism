#!/usr/bin/env python3
"""Exercise camera-language discovery and rejection rules in isolated fixtures."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import validate_camera_language as language


def card(term_id: str = "term-fixture", title: str = "夹具 / Fixture") -> str:
    return f'''<a id="{term_id}"></a>
### {title}

- **分类** Optical Lens & Projection
- **常用别名** `["夹具词", "fixture alias"]`
- **通俗说法** 看见前后空间的变化。
- **专业定义** 按照给定投影和有效画幅定义视角。
- **原理与条件** 保留机位、画幅和镜头条件。
- **可见结果** 画面容纳指定空间。
- **典型场景** 环境人物。
- **常见误解** 焦距与位置分别记录。
- **呈现方式** `directly_visible_in_still`
- **落入现有字段** `镜头`、`机位`，保留原始参数。
- **迁移方法** 根据用户目标调整开放设置。
- **related_equipment_ids** `["lens-fixture"]` [规格](../equipment-library.md#lens-fixture)
- **related_film_card_ids** `["shot-fixture"]` [段落](../cinema-shot-library.md#shot-fixture)
'''


class CameraLanguageValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="camera-language-validator-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "references"
        self.cards = self.root / "camera-language"
        self.cards.mkdir(parents=True)
        self.detail = self.cards / "arbitrary-category.md"
        self.detail.write_text(card(), encoding="utf-8")
        self.index = self.root / "camera-language-dictionary.md"
        self.index.write_text("[夹具](camera-language/arbitrary-category.md#term-fixture)\n", encoding="utf-8")
        (self.root / "equipment-library.md").write_text('<a id="lens-fixture"></a>\n', encoding="utf-8")
        (self.root / "cinema-shot-library.md").write_text('<a id="shot-fixture"></a>\n', encoding="utf-8")
        (self.root / "capture-design.md").write_text(
            "## 摄影记录\n\n| 项目 | 记录内容 |\n| --- | --- |\n| 镜头 | 原值 |\n| 机位 | 距离 |\n", encoding="utf-8"
        )
        self.legacy = self.root / "camera-language-p0.md"
        self.legacy.write_text(
            '<a id="term-fixture"></a>\n[兼容](camera-language/arbitrary-category.md#term-fixture)\n', encoding="utf-8"
        )

    def validate(self) -> tuple[list[str], dict[str, int]]:
        errors: list[str] = []
        stats = language.validate_camera_language(errors, self.root)
        return errors, stats

    def mutate_card(self, old: str, new: str) -> None:
        self.detail.write_text(self.detail.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")

    def assert_rejected(self, diagnostic: str) -> None:
        errors, _ = self.validate()
        self.assertTrue(any(diagnostic in error for error in errors), errors)

    def test_valid_multifile_registry(self) -> None:
        errors, stats = self.validate()
        self.assertEqual([], errors)
        self.assertEqual({"terms": 1, "files": 1, "equipment_edges": 1, "film_edges": 1}, stats)

    def test_new_term_and_new_file_need_no_code_change(self) -> None:
        extra = self.cards / "previously-unknown.md"
        extra.write_text(card("term-extension", "扩展 / Extension"), encoding="utf-8")
        self.index.write_text(
            self.index.read_text(encoding="utf-8") + "[扩展](camera-language/previously-unknown.md#term-extension)\n", encoding="utf-8"
        )
        errors, stats = self.validate()
        self.assertEqual([], errors)
        self.assertEqual(2, stats["terms"])
        self.assertEqual(2, stats["files"])

    def test_additional_card_in_existing_file(self) -> None:
        self.detail.write_text(card() + "\n" + card("term-extra", "新增 / Extra"), encoding="utf-8")
        self.index.write_text(
            self.index.read_text(encoding="utf-8")
            + "[新增](camera-language/arbitrary-category.md#term-extra)\n",
            encoding="utf-8",
        )
        errors, stats = self.validate()
        self.assertEqual([], errors)
        self.assertEqual((2, 1), (stats["terms"], stats["files"]))

    def test_empty_evidence_arrays_are_valid(self) -> None:
        self.mutate_card('`["lens-fixture"]` [规格](../equipment-library.md#lens-fixture)', '`[]`')
        self.mutate_card('`["shot-fixture"]` [段落](../cinema-shot-library.md#shot-fixture)', '`[]`')
        self.assertEqual([], self.validate()[0])

    def test_number_led_english_term_name_is_valid(self) -> None:
        self.mutate_card("夹具 / Fixture", "轴线原则 / 180-degree Rule")
        self.assertEqual([], self.validate()[0])

    def test_aliases_can_overlap_between_concepts(self) -> None:
        self.detail.write_text(card() + "\n" + card("term-other", "另一概念 / Other Concept"), encoding="utf-8")
        self.index.write_text(
            self.index.read_text(encoding="utf-8")
            + "[另一概念](camera-language/arbitrary-category.md#term-other)\n",
            encoding="utf-8",
        )
        self.assertEqual([], self.validate()[0])

    def test_capture_table_is_data_driven(self) -> None:
        capture = self.root / "capture-design.md"
        capture.write_text(capture.read_text(encoding="utf-8") + "| 动态现有字段 | 资料 |\n", encoding="utf-8")
        self.mutate_card('`镜头`、`机位`', '`动态现有字段`')
        self.assertEqual([], self.validate()[0])

    def test_duplicate_index_route(self) -> None:
        self.index.write_text(self.index.read_text(encoding="utf-8") * 2, encoding="utf-8")
        self.assert_rejected("duplicate index route")

    def test_duplicate_card_id_in_other_file(self) -> None:
        (self.cards / "duplicate.md").write_text(card(), encoding="utf-8")
        self.assert_rejected("found 2")

    def test_orphan_card_in_unindexed_file(self) -> None:
        (self.cards / "orphan.md").write_text(card("term-orphan", "孤立 / Orphan"), encoding="utf-8")
        self.assert_rejected("unindexed card")

    def test_missing_card_file(self) -> None:
        self.detail.unlink()
        self.assert_rejected("missing indexed card file")

    def test_missing_card_anchor(self) -> None:
        self.mutate_card('<a id="term-fixture"></a>', "")
        self.assert_rejected("found 0")

    def test_invalid_stable_id(self) -> None:
        self.mutate_card("term-fixture", "term-Bad_ID")
        self.index.write_text(self.index.read_text(encoding="utf-8").replace("term-fixture", "term-Bad_ID"), encoding="utf-8")
        self.assert_rejected("invalid stable term ID")

    def test_outside_reference_route(self) -> None:
        self.index.write_text("[越界](../outside.md#term-fixture)\n", encoding="utf-8")
        self.assert_rejected("escapes the references")

    def test_external_route(self) -> None:
        self.index.write_text("[外部](https://example.org/card.md#term-fixture)\n", encoding="utf-8")
        self.assert_rejected("local Markdown path")

    def test_malformed_url_is_rejected_without_crashing(self) -> None:
        self.index.write_text("[格式错误](https://[/card.md#term-fixture)\n", encoding="utf-8")
        self.assert_rejected("malformed term route")

    def test_non_markdown_route(self) -> None:
        self.index.write_text("[非卡](camera-language/picture.png#term-fixture)\n", encoding="utf-8")
        self.assert_rejected("non-card resource")

    def test_missing_required_field(self) -> None:
        self.mutate_card("- **原理与条件** 保留机位、画幅和镜头条件。\n", "")
        self.assert_rejected("missing or empty field '原理与条件'")

    def test_duplicate_field(self) -> None:
        self.mutate_card("- **典型场景**", "- **分类** Composition\n- **典型场景**")
        self.assert_rejected("duplicate field '分类'")

    def test_invalid_category(self) -> None:
        self.mutate_card("Optical Lens & Projection", "Imaginary Lens Category")
        self.assert_rejected("seven principle dimensions")

    def test_invalid_presentation(self) -> None:
        self.mutate_card("directly_visible_in_still", "all_video_models_verified")
        self.assert_rejected("four presentation tags")

    def test_malformed_alias_json(self) -> None:
        self.mutate_card('["夹具词", "fixture alias"]', '["夹具词",]')
        self.assert_rejected("常用别名 contains invalid JSON")

    def test_unknown_capture_field(self) -> None:
        self.mutate_card('`镜头`、`机位`', '`new_parallel_capture_state`')
        self.assert_rejected("existing Capture Design table field")

    def test_unknown_related_id(self) -> None:
        self.mutate_card('"lens-fixture"', '"lens-unknown"')
        self.assert_rejected("unknown ID 'lens-unknown'")

    def test_duplicate_equipment_library_id_is_rejected(self) -> None:
        library = self.root / "equipment-library.md"
        library.write_text(library.read_text(encoding="utf-8") * 2, encoding="utf-8")
        self.assert_rejected("equipment-library.md: duplicate library stable ID 'lens-fixture'")

    def test_duplicate_film_library_id_is_rejected(self) -> None:
        library = self.root / "cinema-shot-library.md"
        library.write_text(library.read_text(encoding="utf-8") * 2, encoding="utf-8")
        self.assert_rejected("cinema-shot-library.md: duplicate library stable ID 'shot-fixture'")

    def test_known_id_without_link(self) -> None:
        self.mutate_card(" [规格](../equipment-library.md#lens-fixture)", "")
        self.assert_rejected("no matching library link")

    def test_wrong_library_destination(self) -> None:
        self.mutate_card("../equipment-library.md#lens-fixture", "../cinema-shot-library.md#lens-fixture")
        self.assert_rejected("link outside its existing library")

    def test_related_library_query_is_rejected(self) -> None:
        self.mutate_card("../equipment-library.md#lens-fixture", "../equipment-library.md?version=bad#lens-fixture")
        self.assert_rejected("local library link without a query")

    def test_related_library_scheme_is_rejected(self) -> None:
        self.mutate_card("../equipment-library.md#lens-fixture", "file:///equipment-library.md#lens-fixture")
        self.assert_rejected("local library link without a query")

    def test_malformed_related_url_is_rejected_without_crashing(self) -> None:
        self.mutate_card("../equipment-library.md#lens-fixture", "http://[invalid#lens-fixture")
        self.assert_rejected("malformed library link")

    def test_undeclared_linked_id(self) -> None:
        self.mutate_card('`["lens-fixture"]`', '`[]`')
        self.assert_rejected("links undeclared ID")

    def test_legacy_redirect_must_keep_id(self) -> None:
        self.legacy.write_text(
            '<a id="term-fixture"></a>\n[错误](camera-language/arbitrary-category.md#term-other)\n',
            encoding="utf-8",
        )
        self.assert_rejected("same stable ID")

    def test_legacy_page_cannot_be_silently_removed(self) -> None:
        self.legacy.unlink()
        self.assert_rejected("Missing stable-ID compatibility page")

    def test_legacy_page_cannot_drop_all_anchors(self) -> None:
        self.legacy.write_text("# 兼容页\n", encoding="utf-8")
        self.assert_rejected("compatibility page has no stable term anchors")

    def test_fenced_example_is_not_a_card(self) -> None:
        self.detail.write_text(card() + "\n```markdown\n" + card("term-example", "例 / Example") + "```\n", encoding="utf-8")
        self.assertEqual([], self.validate()[0])

    def test_missing_common_resource(self) -> None:
        (self.root / "equipment-library.md").unlink()
        self.assert_rejected("Missing camera-language resource")


if __name__ == "__main__":
    unittest.main(verbosity=2)
