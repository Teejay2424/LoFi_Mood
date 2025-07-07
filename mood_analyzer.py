import re
from transformers import pipeline
from typing import Dict, List
import warnings
warnings.filterwarnings('ignore')

class LofiMoodAnalyzer:
    def __init__(self):
        print("Loading RoBERTa emotion model...")
        self.emotion_classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            return_all_scores=True
        )
        
        self.mood_keywords = {
            'study': [
                'focus', 'homework', 'exam', 'work', 'concentration', 
                'studying', 'productive', 'research', 'coding', 'learning',
                'assignment', 'project', 'deadline', 'finals','study','motivate'
            ],
            'sleep': [
                'tired', 'bedtime', 'sleepy', 'rest', 'peaceful', 
                'drowsy', 'night', 'insomnia', 'bed', 'dream',
                'exhausted', 'wind down', 'late night','sleepy'
            ]
        }
        print("Mood analyzer ready!")
    
    def analyze_emotions(self, text: str) -> Dict[str, float]:
        emotions = self.emotion_classifier(text)[0]
        emotion_scores = {}
        for emotion in emotions:
            if emotion['label'] == 'sadness':
                emotion_scores['sad'] = emotion['score']
            elif emotion['label'] == 'joy':
                emotion_scores['happy'] = emotion['score']
        
        total = emotion_scores.get('sad', 0) + emotion_scores.get('happy', 0)
        if total > 0:
            emotion_scores['sad'] = emotion_scores.get('sad', 0) / total
            emotion_scores['happy'] = emotion_scores.get('happy', 0) / total
        else:
            emotion_scores = {'sad': 0.5, 'happy': 0.5}
            
        return emotion_scores
    
    def detect_keywords(self, text: str) -> Dict[str, int]:
        text_lower = text.lower()
        keyword_counts = {}
        
        for mood, keywords in self.mood_keywords.items():
            count = 0
            for keyword in keywords:
                pattern = r'\b' + re.escape(keyword) + r'\b'
                matches = len(re.findall(pattern, text_lower))
                count += matches
            keyword_counts[mood] = count
        
        return keyword_counts
    
    def combine_scores(self, emotion_scores: Dict[str, float], 
                      keyword_counts: Dict[str, int]) -> Dict[str, float]:
        
        total_keywords = sum(keyword_counts.values())

        if total_keywords > 0:
            emotion_weight = 0.25
            keyword_weight = 0.75
        else:
            emotion_weight = 1
            keyword_weight = 0

        
        final_scores = {}   
        final_scores['sad'] = emotion_scores['sad'] * emotion_weight
        final_scores['happy'] = emotion_scores['happy'] * emotion_weight
        
        if total_keywords > 0:
            for mood, count in keyword_counts.items():
                keyword_score = (count / total_keywords) * keyword_weight
                final_scores[mood] = keyword_score
        else:
            final_scores['sad'] += keyword_weight * emotion_scores['sad']
            final_scores['happy'] += keyword_weight * emotion_scores['happy']
            final_scores['nostalgic'] = 0
            final_scores['study'] = 0
            final_scores['sleep'] = 0
            final_scores['chill'] = 0
        
        for mood in ['sad', 'happy', 'nostalgic', 'study', 'sleep', 'chill']:
            if mood not in final_scores:
                final_scores[mood] = 0
        
        total = sum(final_scores.values())
        if total > 0:
            final_scores = {mood: (score/total) * 100 
                          for mood, score in final_scores.items()}
        
        return final_scores
    
    def analyze_mood(self, user_input: str) -> Dict[str, float]:
        print(f"\nAnalyzing: '{user_input}'")
        
        emotion_scores = self.analyze_emotions(user_input)
        print(f"Emotions detected: {emotion_scores}")
        
        keyword_counts = self.detect_keywords(user_input)
        print(f"Keywords found: {keyword_counts}")
        keyword_counts = self.detect_keywords(user_input)
        print(f"Keywords found: {keyword_counts}")
        
        
        final_moods = self.combine_scores(emotion_scores, keyword_counts)
        
        return final_moods



    
   
    
        print("Final Mood Breakdown:")
        for mood, percentage in sorted(mood_percentages.items(), 
                                     key=lambda x: x[1], reverse=True):
            if percentage > 0:
                print(f"  {mood.capitalize()}: {percentage:.1f}%")
        print()

if __name__ == "__main__":
    demo_analyzer()