# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Rhythm

---

## 2. Intended Use  

It suggests the top 5 songs from a small catalog based on a listener's favorite genre and mood, plus targets for energy and other features. It assumes the listener can state their taste up front and that it stays the same from one session to the next. It's for classroom exploration only, not real users.

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

The catalog has 19 songs across 16 genres and 14 moods. I added 9 songs to the original 10 (hip hop, classical, country, metal, r&b, reggae, edm, folk, latin) and removed none. It's still tiny, and it's missing things like lyrics, language, era, artist popularity, and anything about how people actually listen.

---

## 5. Strengths  

It works well when a listener's preferences agree with each other, like the pop, happy, energy 0.8 profile, which put Sunrise City and Rooftop Lights on top. Scoring by closeness also separates calm from intense songs correctly, and lofi/chill returned lofi chill tracks first, which matched my intuition. The reasons list makes every result easy to explain.

---

## 6. Limitations and Bias 

The biggest weakness I found is that the score is dominated by energy so the system can trap a listener in one same band/vibe regardless of what else they asked for. Energy can earn up to 2.0 points and valence up to 1.0, while a mood match is worth at most 1.5, so the numbers can outvote the label. When I tested a profile with mood "sad" but high energy (0.95) and high valence (0.9), four upbeat pop, latin and edm songs ranked ahead of every sad song, and the only sad song, Autumn Letters, barely made the list at fifth. A listener who wants a sad song and happens to set a high energy target is never shown the kind of music they named, which is a small filter bubble, since the results keep reflecting the numeric target and ignore the mood the listener actually asked for. SInce moods and genres appear on only one to three songs each in this catalog, listeners with unusual tastes get scored on energy alone, so they are also served the narrowest set of results.

---

## 7. Evaluation  

I ran the recommender on a normal profile plus eight weird ones and read the top 5 and the reasons for each. Full output is in the README.

**Profiles tested:** baseline (pop, happy, energy 0.8), conflicting (sad mood but high energy and valence), empty, genre/mood not in the catalog, energy 1.5, energy -0.5, case mismatch ("Pop"/"HAPPY"), mid-everything (0.5 on every number), and label-only (lofi, chill).

**What was off**

- The baseline looked right. Sunrise City won because it matched everything.
- The empty profile gave every song 0.00, so the "top 5" was just the first five rows in the file.
- Capitalization broke the case-mismatch profile. The genre and mood bonuses just quietly vanished.
- Out-of-range energy (1.5 or -0.5) was accepted with no complaint, and scores shrank for no good reason.
- The conflicting profile put four upbeat songs ahead of the only sad one.
- Mid-everything got the highest score of all (3.61) from a listener with no real taste.
- Label-only had a tie at 2.50 that file order decided, and its #5 matched nothing.
- Genres and moods that aren't in the catalog just fell back to energy.

**Comparing three profiles** (baseline, case mismatch, conflicting)

- *Baseline vs. case mismatch:* Same listener, only the capital letters differ, but the top score dropped from 4.46 to 1.96 and Gym Hero fell out of the top 5. Sunrise City still came first, but only because of its energy, and it tied with a hip hop song that matches neither genre nor mood. So the labels do a lot of the work, and a typo wipes it out.
- *Baseline vs. conflicting:* Labels drive the baseline and the numbers drive the conflicting one. Sunrise City won the baseline on everything but only came fourth in the conflicting list. The one sad song only made it to #5 thanks to its mood bonus.
- *Case mismatch vs. conflicting:* Both end up as upbeat songs ranked by energy, but the causes differ. One is a bug (text comparison) and the other is a design choice (numbers outweigh mood).

**What surprised me:** tiny things like a capital letter or a missing preference changed the results a lot, and the scores gave no hint anything was wrong. The reasons list is what made the problems easy to spot.

---

## 8. Future Work  

I would clean up inputs (lowercase labels, clamp numbers to 0-1, handle empty profiles) and give partial credit to related moods and genres like chill and relaxed. Id also add tempo and artist as features and a diveristy step so the top 5 aren't all near-identical. To handle more complex tastes, a listener could have several profiles, like workout and study.

---

## 9. Personal Reflection  

I learned that a recommender is really just a pile of choices about which features count and how much, and those choices decide who gets good results. The most surprising part was how much tiny details like a capital letter or an unset preference changed the output. It makes me think app recommendations reflect their weights and data, not some neutral read on my taste.
