import csv
import heapq
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dicts with numeric fields converted."""
    print(f"Loading songs from {csv_path}...")
    int_fields = ("id",)
    float_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")

    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            for field in int_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

# Maximum points each feature can contribute (a perfect match earns the full amount).
CATEGORICAL_POINTS = {"mood": 1.5, "genre": 1.0}
NUMERIC_POINTS = {"energy": 2.0, "valence": 1.0, "danceability": 0.5, "acousticness": 0.5}

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences, returning (score, reasons)."""
    score = 0.0
    reasons: List[str] = []

    # Categorical features: full points on an exact match, nothing otherwise.
    for feature, points in CATEGORICAL_POINTS.items():
        if feature in user_prefs and song[feature] == user_prefs[feature]:
            score += points
            reasons.append(f"{feature} matches '{song[feature]}' (+{points:.2f})")

    # Numeric features: points scale with closeness to the target, not raw value.
    for feature, max_points in NUMERIC_POINTS.items():
        if feature not in user_prefs:
            continue
        closeness = max(0.0, 1.0 - abs(song[feature] - user_prefs[feature]))
        points = max_points * closeness
        score += points
        reasons.append(
            f"{feature} {song[feature]:.2f} vs target {user_prefs[feature]:.2f} (+{points:.2f})"
        )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs as (song, score, explanation), highest score first."""
    def scored_entry(song: Dict) -> Tuple[Dict, float, str]:
        """Pair a song with its score and a joined explanation string."""
        score, reasons = score_song(user_prefs, song)
        return song, score, "; ".join(reasons)

    # nlargest keeps only k items (O(n log k)) and returns them highest-first.
    return heapq.nlargest(k, map(scored_entry, songs), key=lambda entry: entry[1])
