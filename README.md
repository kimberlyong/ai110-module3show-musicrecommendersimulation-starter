# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This version loads a catalog of 19 songs, scores each one against a listener's favorite genre, mood and numeric targets like energy, and recommends the top 5 with the reasons behind each score. It scores numbers by closeness to the target, not by raw value, and gives fixed bonuses for mood and genre matches.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Each song is scored by how closely it matches the user's taste profile, and the highest-scoring songs are recommended.

**Song features:** genre, mood, energy, valence, danceability, acousticness, tempo.

**UserProfile:** stores a preferred genre, a preferred mood, and target values for the numeric features (for example, target energy 0.8).

**Scoring:** the score is a weighted sum of per-feature similarity.
- *Numeric features* (energy, valence, etc.) score by closeness to the user's target, not by raw value. A song with energy 0.35 scores well for a user who wants 0.3, even though 0.9 is "higher."
- *Mood and genre* add a bonus when they match the profile.
- *Weights:* energy and mood count most because energy is specific and quantitative and mood reflects the listening situation. The other features contribute smaller amounts.

**Choosing recommendations:** every song in the catalog is scored, the songs are sorted from highest to lowest, and the top 5 are returned along with a breakdown of why each one scored as it did.

This system might limit if a user wants to listen to songs of a different genre or are interested in multiple different types of music. This could result in conflicting data that instead produces recommendations that are too varied.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
         Profile: genre=pop, mood=happy, energy=0.8         
============================================================

#1  Sunrise City                             Score:  4.46
------------------------------------------------------------
  - mood matches 'happy' (+1.50)
  - genre matches 'pop' (+1.00)
  - energy 0.82 vs target 0.80 (+1.96)

#2  Rooftop Lights                           Score:  3.42
------------------------------------------------------------
  - mood matches 'happy' (+1.50)
  - energy 0.76 vs target 0.80 (+1.92)

#3  Gym Hero                                 Score:  2.74
------------------------------------------------------------
  - genre matches 'pop' (+1.00)
  - energy 0.93 vs target 0.80 (+1.74)

#4  Concrete Crown                           Score:  1.96
------------------------------------------------------------
  - energy 0.78 vs target 0.80 (+1.96)

#5  Calle Fuego                              Score:  1.90
------------------------------------------------------------
  - energy 0.85 vs target 0.80 (+1.90)

============================================================
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

I ran the recommender on eight edge-case profiles (conflicting preferences, empty, unknown genre and mood, out-of-range energy, case mismatch, and others) and compared the results with the baseline pop/happy profile. I didn't try changing the weights or adding tempo, so those are left for future work.

### Adversarial and edge-case profiles

Each profile below was run through the recommender (top 5 shown).

**Conflicting preferences (sad mood, high energy, high valence)**

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
        Profile: mood=sad, energy=0.95, valence=0.9         
============================================================

#1  Pulse Horizon                            Score:  2.97
------------------------------------------------------------
  - energy 0.94 vs target 0.95 (+1.98)
  - valence 0.89 vs target 0.90 (+0.99)

#2  Gym Hero                                 Score:  2.83
------------------------------------------------------------
  - energy 0.93 vs target 0.95 (+1.96)
  - valence 0.77 vs target 0.90 (+0.87)

#3  Calle Fuego                              Score:  2.76
------------------------------------------------------------
  - energy 0.85 vs target 0.95 (+1.80)
  - valence 0.86 vs target 0.90 (+0.96)

#4  Sunrise City                             Score:  2.68
------------------------------------------------------------
  - energy 0.82 vs target 0.95 (+1.74)
  - valence 0.84 vs target 0.90 (+0.94)

#5  Autumn Letters                           Score:  2.62
------------------------------------------------------------
  - mood matches 'sad' (+1.50)
  - energy 0.31 vs target 0.95 (+0.72)
  - valence 0.30 vs target 0.90 (+0.40)

============================================================
```

**Empty profile**

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
                      Profile: (none)                       
============================================================

#1  Sunrise City                             Score:  0.00
------------------------------------------------------------

#2  Midnight Coding                          Score:  0.00
------------------------------------------------------------

#3  Storm Runner                             Score:  0.00
------------------------------------------------------------

#4  Library Rain                             Score:  0.00
------------------------------------------------------------

#5  Gym Hero                                 Score:  0.00
------------------------------------------------------------

============================================================
```

**Genre and mood not in the catalog**

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
       Profile: genre=k-pop, mood=dreamy, energy=0.6        
============================================================

#1  Velvet Hours                             Score:  1.90
------------------------------------------------------------
  - energy 0.55 vs target 0.60 (+1.90)

#2  Island Breeze                            Score:  1.84
------------------------------------------------------------
  - energy 0.52 vs target 0.60 (+1.84)

#3  Dusty Porch Swing                        Score:  1.76
------------------------------------------------------------
  - energy 0.48 vs target 0.60 (+1.76)

#4  Night Drive Loop                         Score:  1.70
------------------------------------------------------------
  - energy 0.75 vs target 0.60 (+1.70)

#5  Rooftop Lights                           Score:  1.68
------------------------------------------------------------
  - energy 0.76 vs target 0.60 (+1.68)

============================================================
```

**Out-of-range energy (1.5)**

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
                    Profile: energy=1.5                     
============================================================

#1  Iron Requiem                             Score:  0.94
------------------------------------------------------------
  - energy 0.97 vs target 1.50 (+0.94)

#2  Pulse Horizon                            Score:  0.88
------------------------------------------------------------
  - energy 0.94 vs target 1.50 (+0.88)

#3  Gym Hero                                 Score:  0.86
------------------------------------------------------------
  - energy 0.93 vs target 1.50 (+0.86)

#4  Storm Runner                             Score:  0.82
------------------------------------------------------------
  - energy 0.91 vs target 1.50 (+0.82)

#5  Calle Fuego                              Score:  0.70
------------------------------------------------------------
  - energy 0.85 vs target 1.50 (+0.70)

============================================================
```

**Negative energy (-0.5)**

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
                    Profile: energy=-0.5                    
============================================================

#1  Moonlight Sonata Reimagined              Score:  0.64
------------------------------------------------------------
  - energy 0.18 vs target -0.50 (+0.64)

#2  Spacewalk Thoughts                       Score:  0.44
------------------------------------------------------------
  - energy 0.28 vs target -0.50 (+0.44)

#3  Autumn Letters                           Score:  0.38
------------------------------------------------------------
  - energy 0.31 vs target -0.50 (+0.38)

#4  Library Rain                             Score:  0.30
------------------------------------------------------------
  - energy 0.35 vs target -0.50 (+0.30)

#5  Coffee Shop Stories                      Score:  0.26
------------------------------------------------------------
  - energy 0.37 vs target -0.50 (+0.26)

============================================================
```

**Case mismatch (Pop / HAPPY)**

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
         Profile: genre=Pop, mood=HAPPY, energy=0.8         
============================================================

#1  Sunrise City                             Score:  1.96
------------------------------------------------------------
  - energy 0.82 vs target 0.80 (+1.96)

#2  Concrete Crown                           Score:  1.96
------------------------------------------------------------
  - energy 0.78 vs target 0.80 (+1.96)

#3  Rooftop Lights                           Score:  1.92
------------------------------------------------------------
  - energy 0.76 vs target 0.80 (+1.92)

#4  Calle Fuego                              Score:  1.90
------------------------------------------------------------
  - energy 0.85 vs target 0.80 (+1.90)

#5  Night Drive Loop                         Score:  1.90
------------------------------------------------------------
  - energy 0.75 vs target 0.80 (+1.90)

============================================================
```

**Mid-everything (0.5 on every numeric target)**

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
Profile: energy=0.5, valence=0.5, danceability=0.5, acousticness=0.5
============================================================

#1  Midnight Coding                          Score:  3.61
------------------------------------------------------------
  - energy 0.42 vs target 0.50 (+1.84)
  - valence 0.56 vs target 0.50 (+0.94)
  - danceability 0.62 vs target 0.50 (+0.44)
  - acousticness 0.71 vs target 0.50 (+0.40)

#2  Dusty Porch Swing                        Score:  3.55
------------------------------------------------------------
  - energy 0.48 vs target 0.50 (+1.96)
  - valence 0.68 vs target 0.50 (+0.82)
  - danceability 0.64 vs target 0.50 (+0.43)
  - acousticness 0.81 vs target 0.50 (+0.34)

#3  Focus Flow                               Score:  3.52
------------------------------------------------------------
  - energy 0.40 vs target 0.50 (+1.80)
  - valence 0.59 vs target 0.50 (+0.91)
  - danceability 0.60 vs target 0.50 (+0.45)
  - acousticness 0.78 vs target 0.50 (+0.36)

#4  Island Breeze                            Score:  3.50
------------------------------------------------------------
  - energy 0.52 vs target 0.50 (+1.96)
  - valence 0.80 vs target 0.50 (+0.70)
  - danceability 0.78 vs target 0.50 (+0.36)
  - acousticness 0.55 vs target 0.50 (+0.47)

#5  Velvet Hours                             Score:  3.49
------------------------------------------------------------
  - energy 0.55 vs target 0.50 (+1.90)
  - valence 0.73 vs target 0.50 (+0.77)
  - danceability 0.76 vs target 0.50 (+0.37)
  - acousticness 0.40 vs target 0.50 (+0.45)

============================================================
```

**Label-only (lofi / chill)**

```
============================================================
                   TOP 5 RECOMMENDATIONS                    
              Profile: genre=lofi, mood=chill               
============================================================

#1  Midnight Coding                          Score:  2.50
------------------------------------------------------------
  - mood matches 'chill' (+1.50)
  - genre matches 'lofi' (+1.00)

#2  Library Rain                             Score:  2.50
------------------------------------------------------------
  - mood matches 'chill' (+1.50)
  - genre matches 'lofi' (+1.00)

#3  Spacewalk Thoughts                       Score:  1.50
------------------------------------------------------------
  - mood matches 'chill' (+1.50)

#4  Focus Flow                               Score:  1.00
------------------------------------------------------------
  - genre matches 'lofi' (+1.00)

#5  Sunrise City                             Score:  0.00
------------------------------------------------------------

============================================================
```

---

## Limitations and Risks

The catalog is tiny, so most genres and moods match only one or two songs, and the score leans heavily on energy, which can drown out mood and genre. It also ignores lyrics and language, treats labels as exact matches only, and doesn't validate input, so typos or empty profiles give misleading results.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Building this showed me that a recommender turns data into predictions with a handful of design choices: which features count, how much each one is worth, and how "similar"is measured. Scoring by closeness to a target instead of raw value made the results feel more sensible and the reasons list made it easy to see why each song was picked. The weights were just my first guesses, but they decided everything about what rose to the top.

Bias showed up minimally. Energy was hte main factor so a listener who asked for a sad mood but a high energy target mostly got upbeat songs, and a capital letter in a genre removed a bonus. With a tiny catalog where most moods and genres appear only once or twice, listeners with unusual tastes get thinner results than mainstream ones. Real recommenders have the same problem at a much larger scale, and the people affected rarely get a reasons list to spot it.



