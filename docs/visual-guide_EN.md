# Dream Director · Visual Methods and Historical Work

These are the author's existing AIGC examples, not regenerated v2.4 results or evidence of improved strength control or interaction.

[Back to README](../README_EN.md) · [Director strength rules](../zy-cinematic-realism/references/director-routing.md)


## Continuity: Base Lock + Shot Delta

For an eight-shot sequence about an urban woman knight leaving work, start with a `Continuity Bible` that locks her face, silver commuter armor, worn canvas bag, folding spear, station, and cool/warm practical light sources. Every shot combines the same `Base Lock` with one limited `Shot Delta` describing only the new action, camera, or time change.

This reduces drift in faces, clothing, props, locations, and lighting. It does not promise identical model outputs; it makes every change traceable.

<a id="prompt-doctor"></a>
## Prompt Doctor: Repair, Do Not Rewrite

When a result looks like a commercial, the problem is usually not a lack of “cinematic” words. The camera may be too frontal, the character may be posing, or the key and supporting light may have no hierarchy. Prompt Doctor diagnoses the result before producing a scoped repair instruction:

```text
CHANGE ONLY: camera position, posing, and light hierarchy.
PRESERVE EXACTLY: identity, wardrobe, car, and location.
```

Repair is not a new creative pass. Character identity, wardrobe, vehicle, and location remain anchored to the original Scene Master. Only named variables may change.

<a id="creative-grammar"></a>
## Creative Grammar: Executable Decisions, Not Filters

v2.0.0 preserves the Four-Axis Visual Fingerprints for 38 directors and adds 16 style cards plus 8 cinematography cards. These cards alter light, exposure, camera, space, blocking, and visual center instead of appending a style label.

- Style cards provide controlled directions such as austere realism, wet noir, quiet everyday life, or institutional pressure.
- Cinematography cards provide witness positions such as outside a doorway, close but obstructed, distant negative space, or a procedural locked-off camera.
- Director references continue to shape contrast, color and exposure, camera position, and composition without copying any specific film shot.

Technical camera details come last. They strengthen a story moment that already works; they do not replace the story.

## Choose a Different Moment from the Same Story

The Skill does more than apply filters to one composition. It helps decide which moment in the story deserves to be seen.

### The interrogation is slipping out of control

![An interrogation slipping out of control, observed through one-way glass](images/scene-interrogation.webp)

The camera is not seated at the negotiation table. It watches through one-way glass. Reflections, monitoring equipment, and large dark areas make the audience feel like an observer who should not be there.

### The case follows him home

![A detective reading files alone in his apartment late at night](images/scene-private-aftermath.webp)

The character does not need to cry or shout. A letter on the desk, unfinished coffee, a doorway obstruction, and one table lamp are enough to show that he still cannot let go.

### Silence after the truth

![Two detectives standing small inside the negative space of a riverfront](images/scene-river-silence.webp)

The characters become small and move away from center while the city and river occupy most of the frame. The environment no longer serves as background; it speaks for them.

### The protagonist leaves; the city continues

![A police car receding along a city street at dawn](images/scene-city-finale.webp)

An ending does not require a close-up of the protagonist. Seen through scratched glass, the police car disappears as ordinary people begin a new day. The story is over, but the city has not stopped.

## The Method Works Across Genres

![A boxer caught at the instant of impact through the ring ropes](images/scene-boxer-corner.webp)

Action does not require a clean, complete heroic composition. Foreground ropes and an opponent's body obstruct the view; slight motion blur preserves the speed of impact; the subject may not even be perfectly focused. It feels like a frame the camera managed to catch during the fight, not a sports advertisement.

The same method works for crime, boxing, family drama, science fiction, historical stories, and urban shorts. The principle remains:

> **Do not stop at “two boxers fighting intensely.” Specify the round, the fraction of a second before or after impact, what the camera sees through, and how much motion blur should remain.**

<a id="director-method"></a>
## Reobserve the Same Story Through a Director's Method

### Director Four-Axis Visual Fingerprint System

Director files translate methods into current-scene decisions instead of appending names and titles. The four axes are an internal planning and checking structure. When you request a breakdown, inspect:

1. `Lighting and contrast signature`
2. `Color and exposure signature`
3. `Lens and camera signature`
4. `Composition and spatial signature`

Each applicable axis describes a concrete decision, and locked axes may remain unchanged. Use the requested strength; strong mode seeks structural distinction only in open axes and viewing decisions, without quotas on locked action, camera, or composition. The model adapter controls final syntax and density; a labeled block is not mandatory. Active decisions should remain executable after removing names and titles.

The same story therefore changes in light, color, camera, and composition while preserving the user's period, location, characters, event, physical space, and motivated light. Representative works are model-recognition anchors only; the system does not copy any specific scene.

| Region | Selected directors | Most visible four-axis direction |
|---|---|---|
| Chinese-language cinema | Zhang Yimou, Jia Zhangke, Wong Kar-wai, Hou Hsiao-hsien, Edward Yang, Diao Yinan | From ritual color order to social transition, subjective cities, and layered everyday life |
| Japanese cinema | Akira Kurosawa, Yasujirō Ozu, Shunji Iwai, Hirokazu Kore-eda, Kiyoshi Kurosawa | From weather-driven action axes to domestic space, seasonal memory, and unseen threat |
| Korea and Southeast Asia | Bong Joon-ho, Park Chan-wook, Lee Chang-dong, Apichatpong Weerasethakul | From class space and object desire to moral observation and tropical time |
| European auteurs | Andrei Tarkovsky, Stanley Kubrick, Alfred Hitchcock, Ingmar Bergman | From elemental memory and institutional geometry to gaze-based suspense and facial relationships |
| American genre and auteur cinema | David Fincher, David Lynch, Martin Scorsese, Francis Ford Coppola, Michael Mann | From procedural information and psychological disturbance to street systems, family power, and nocturnal professional networks |
| Contemporary international cinema | Christopher Nolan, Denis Villeneuve, Terrence Malick, Alfonso Cuarón, Chloé Zhao | From physical mechanisms and environmental scale to bodily tactility, continuous social space, and working landscapes |

[Browse the full index of 38 directors, aliases, and four-axis summaries](../zy-cinematic-realism/references/directors/index.md) · [Choose directors by scene goal with the recommendation matrix](../zy-cinematic-realism/references/directors/recommendation-matrix.md)

```text
Use $zy-cinematic-realism:

Late 1990s, a small city in southern China. A young police officer searches
a video rental shop during a blackout for a tape left by a missing person.

Director reference: Diao Yinan
Style strength: strong

Make the director's light and contrast, color and exposure, camera distance,
and spatial composition distinct, explicit, and non-interchangeable.
Do not copy any specific film scene.
```

> v2.4 respects subtle / clear / strong strength; unspecified strength defaults to clear. Locked action, camera, and composition are not reselected for differentiation. Images below retain their historical strong-mode labels.

### Four directors, one fixed scene

The story fact remains “searching for a tape inside a video store during a blackout”:

| Director | Light | Color and exposure | Camera | Composition and space |
|---|---|---|---|---|
| Diao Yinan | Green emergency lamps and a red exit sign form isolated hard pools of light | Tired skin, dense blacks, practical sources cutting through the frame | A slightly delayed observational medium-wide shot, panning only after the action | Departing customers and seats fragment the officer; danger remains inside public order |
| David Fincher | Low illumination preserves legibility on the tape, hand, and logbook | Neutral-cool response, controlled paper white, precise falloff in secondary zones | An exact medium shot from the doorway with minimal movement; focus connects information nodes | Tape, record, and gesture form a traceable evidence chain |
| Wong Kar-wai | Fluorescent light, exit light, and rain-soaked exterior light contaminate one another | Mixed color casts, local underexposure, slight drift around practical highlights | Compressed or mildly distorted close observation through glass or seating | Reflection and obstruction turn the search into a private missed encounter |
| Edward Yang | The store, corridor, and street retain ordinary practical light | Honest fluorescent and urban material colors without an emotional filter | A clear medium-long view from the adjacent room or ticket counter, retaining context | Architecture separates officer, clerk, and departing customers; social relationships outweigh the tape |

## What Would Different Directors See in the Same Story?

This stress test locks the same story, characters, period, location, and evidence, changing only the director reference. v2.0.0 preserves those structural differences and forces every direction into four consecutive signatures—contrast, color and exposure, camera position, and composition—so models are less likely to collapse the result into one generic style sentence.

The difference is not a filter on the same image. Each director makes a new decision about what the shot is actually watching.

Fixed scene: mid-1980s Manhattan, late at night in a police evidence room. A tired detective compares a city garage employee card with a black-and-white surveillance projection on the wall.

<table>
  <tr>
    <td width="50%" align="center">
      <img src="images/director-style-comparison/baseline.webp" alt="No-director baseline in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>No-director baseline</strong>
      <br>
      <sub>Grounded investigative action, plausible camera, practical light</sub>
    </td>
    <td width="50%" align="center">
      <img src="images/director-style-comparison/wong-kar-wai.webp" alt="Strong Wong Kar-wai mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>Wong Kar-wai</strong>
      <br>
      <sub>Subjective time, obstructed reflections, unfinished nocturnal relationships</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="images/director-style-comparison/stanley-kubrick.webp" alt="Strong Stanley Kubrick mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>Stanley Kubrick</strong>
      <br>
      <sub>Institutional geometry, cool distance, unease inside order</sub>
    </td>
    <td width="50%" align="center">
      <img src="images/director-style-comparison/denis-villeneuve.webp" alt="Strong Denis Villeneuve mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>Denis Villeneuve</strong>
      <br>
      <sub>Spatial pressure, negative space, small figures inside environment</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <img src="images/director-style-comparison/david-fincher.webp" alt="Strong David Fincher mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>David Fincher</strong>
      <br>
      <sub>Procedural information, exact camera position, controlled evidence hierarchy</sub>
    </td>
    <td width="50%" align="center">
      <img src="images/director-style-comparison/terrence-malick.webp" alt="Strong Terrence Malick mode in a 1980s New York police evidence room" width="100%">
      <br>
      <strong>Terrence Malick</strong>
      <br>
      <sub>Bodily pauses, tactile interruption, incomplete projected moments</sub>
    </td>
  </tr>
</table>

| Version | What the shot primarily watches |
|---|---|
| No-director baseline | How the detective compares the employee card with the surveillance projection |
| Wong Kar-wai | Late-night isolation, reflection, obstruction, and an incomplete psychological relationship |
| Stanley Kubrick | How the individual is controlled by institutional space and geometric order |
| Denis Villeneuve | How a small detective faces an evidence system heavier than himself |
| David Fincher | How cards, projection, photographs, and text form a precise information chain |
| Terrence Malick | How a tired body, paper edges, sleeves, and projection light interrupt procedural action |

> Every version preserves the same story facts. The differences come from reselecting the moment, visual center, camera, blocking, light, depth of field, and texture.

[View all six invocation examples, Final Prompts, and Avoid blocks](director-style-comparison.md)
