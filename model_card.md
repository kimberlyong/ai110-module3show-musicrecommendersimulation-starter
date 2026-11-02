# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

The recommender works like a points game. Every song in the catalog is compared with a short description of what the listener wants, and it earns points for each way it matches. The songs with the most points are recommended.

**What the listener tells the system.** A listener gives a favorite genre, a favorite mood, and a target for how energetic the music should be (for example, 0.8 on a scale from 0 to 1). They can also give targets for how upbeat, danceable, or acoustic they want the music to be.

**What the system looks at in each song.** Genre, mood, energy, how positive the song feels (valence), danceability, and acousticness. A song's tempo is stored in the data but is not used in the score, because it mostly repeats what energy already says.

**How points are earned.** There are two kinds of features:

- *Labels* (mood and genre) are all or nothing. If the song's mood is the one the listener asked for, it gets 1.5 points. If its genre matches, it gets 1.0 point. Otherwise it gets zero for that feature.
- *Numbers* (energy, valence, danceability, acousticness) reward closeness, not size. A song earns most of the available points when it is near the listener's target, and fewer as it drifts away. A higher number is not automatically better. If someone wants calm music at 0.3 energy, a 0.35 song beats a 0.9 song. Energy is worth the most (up to 2.0 points), valence is worth up to 1.0, and danceability and acousticness are worth up to 0.5 each.

A feature only counts if the listener gave a preference for it, so a listener who only names a genre, mood, and energy is scored on just those three.

**Choosing what to recommend.** The system adds up each song's points, ranks all songs from highest to lowest, and shows the top five. Each recommendation also lists the reasons behind its score, such as "mood matches 'happy' (+1.50)", so a listener can see why a song was picked.

**Why these weights.** Energy gets the most weight because it separates calm and intense songs clearly and is easy for a listener to describe. Mood comes next because it describes the situation the listener is in. Genre counts for less because the catalog is small and most genres have only one or two songs. The weights are a first guess, not a tuned result, and changing them would change which songs rise to the top.

**What changed from the starter.** The starter code only returned the first few songs in the file without looking at the listener at all. This version loads the full catalog, scores every song against the listener's preferences, ranks them, and explains each result.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
