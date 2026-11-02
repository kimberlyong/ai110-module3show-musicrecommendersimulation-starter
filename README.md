# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



