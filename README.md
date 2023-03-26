# Dark Songs

Introducing the most modern and challenging way to play through Dark Souls,

Prepare To Sing!

## Installation

+ Download your preferred version on the [release page](https://github.com/TheodoreChristianRadu/DarkSongs/releases)
+ From the extracted archive, run **Driver.exe** to install the necessary driver
+ Launch **DarkSongs.exe** from the *DarkSongs* folder

## Versions

There are currently two versions of the software:
+ The original *interval version* will detect each change in pitch and perform an in-game action based on the interval ratio to the previous note.
+ The updated *tonal version* will simply detect the current pitch and compare it to a chosen fundamental to identify the tone on a relative scale and perform an in-game action for each new tone sung. In order to compensate for the need for *perfect pitch*, this version was added the ability to play a string accompaniment on the requested fundamental.

## Ratios

By default, the ratios for intervals respectively tones were calculated by the following formula corresponding to *equal temperament*:
$$ratio = 2^{i/12} \\, for \\: i \in [-12, 12]$$
Intervals respectively tones can be added by editing **Intervals.json** respectively **Tones.json**.
As an example, to add the ability to detect *Minor Ninths*, one would modify **Intervals.json** thusly:
```
{
    "Minor Ninth Up": 2.1189261887185906,
    "Octave Up": 2.0,
    [...]
    "Unison": 1.0,
    [...]
    "Octave Down": 0.5,
    "Minor Ninth Down": 0.47193715634084676
}
```
Beware, however, when editing **Intervals.json** to always keep the *Unison* included as it is the default interval returned when no change in pitch occurs.

## Actions

The possible actions to be performed in-game are defined in **Actions.json**. The default ones were defined with Dark Souls in mind, however, they can be adapted to any game playable with an Xbox 360 Controller.
Each action is given a name and a list of successive commands to execute as such:
```"Name": ["Press A", "Wait 0.1", "Release A"]```
Commands are strings of characters enclosed between quotation marks. They can be of the following forms:
+ `"Press Button"` or `"Release Button"` where `Button` can be `A`, `B`, `X`, `Y`, `LB`, `RB`, `LT`, `RT`, `LSB`, `RSB`, `DPU`, `DPD`, `DPR`, `DPL`, `START` or `BACK`
+ `Press Stick Direction` or `Release Stick` where `Stick` can be `LS` or `RS` and `Direction` must be defined as a list of **horizontal** and **vertical** values under *Directions*
+ `Wait T` where `T` is a value corresponding to the time to wait in seconds

## Configuration

The main configuration can be changed both from the software's interface and by manually editing **Configuration.json**.
+ The *Mappings* assign an action from **Actions.json** to each interval respectively tone from **Intervals.json** respectively **Tones.json**.
+ The *Note Duration* parameter determines how often note detections occur in seconds. Too high the value and the game will feel nonresponsive and your notes will have to last quite long, too low the value and the detection will become imprecise. Keep it between 0.1 and 0.5 for reasonable results.
+ In the *interval version*, the *Minimum Frequency* and *Maximum Frequency* parameters determine the minimum and maximum pitch in hertz that may be detected from your voice. Set them depending on your vocal range. In the *tonal version*, these are calculated based on the lowest and highest tones defined.
+ In the *tonal version*, the *Fundamental Frequency* parameter determines the reference frequency in hertz to which your voice will be compared. It is the tonal center of your song. Set it to the note you feel the most comfortable singing.
+ In the *tonal version*, the *Output Volume* parameter determines the volume of the string accompaniment to be played between 0 and 100. If you have perfect pitch, set it to 0.
