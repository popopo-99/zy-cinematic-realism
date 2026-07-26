# Director Lens Library

## When to use

Use this library only when the user explicitly names a director, asks for a director's visual method, asks to compare directions, or asks for a suitable director recommendation.

## Default behavior

- Default strength: `Clear`.
- No named director means no director reference.
- Use one director by default.
- Read only the references needed for the task: exactly one matching reference for a single named director, two or three candidates for a comparison or recommendation, or no more than the primary and secondary references for an explicit mix.
- Convert the method into visual decisions; never use a name as shorthand for those decisions.

## Style strength

### Subtle

Influence only a few choices in story beat, composition, or light.

### Clear

Clearly influence story beat, character action, camera position, and spatial relationship. This is the default.

### Strong

Let the method shape the whole image logic, without reproducing a specific film scene.

## Mixing

Allow at most one primary and one secondary director, and only on explicit request. The secondary director may control one stated dimension only, such as weather pressure, camera distance, character intimacy, spatial geometry, or movement rhythm.

## Output rule

Do not include director names, film names, `in the style of`, or `directed by` in the Final Prompt by default. Preserve user-fixed era, location, characters, event, weather, and composition. Keep light motivated and physical.
