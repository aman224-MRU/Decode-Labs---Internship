"""Simple Movie Recommendation System - Single File"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from pathlib import Path


class MovieRecommender:
    """Simple movie recommendation using TF-IDF similarity."""
    
    def __init__(self):
        print("\n🎬 Loading movies...")
        self.movies = pd.read_csv("movies.csv")
        
        print("🔄 Building recommendation model...")
        # Create text features from title and genres
        self.movies['features'] = self.movies['title'] + ' ' + self.movies['genres'].fillna('')
        
        # Build TF-IDF model
        self.vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
        self.tfidf_matrix = self.vectorizer.fit_transform(self.movies['features'])
        print(f"✓ Loaded {len(self.movies)} movies\n")
    
    def get_recommendations(self, movie_name, num_results=8):
        """Get similar movies based on input movie name."""
        # Find the movie
        matches = self.movies[
            self.movies['title'].str.contains(movie_name, case=False, na=False, regex=False)
        ]
        
        if matches.empty:
            return None
        
        # Get the first match index
        movie_idx = matches.index[0]
        input_movie = matches.iloc[0]['title']
        
        # Calculate similarity scores
        similarities = cosine_similarity(self.tfidf_matrix[movie_idx], self.tfidf_matrix)[0]
        
        # Get top results (excluding the input movie)
        top_indices = np.argsort(similarities)[::-1][1:num_results+1]
        
        # Create results dataframe
        results = self.movies.iloc[top_indices].copy()
        results['score'] = similarities[top_indices]
        results = results.sort_values('score', ascending=False)
        
        return input_movie, results


def main():
    """Main function to run the recommendation system."""
    print("=" * 60)
    print("🎬 MOVIE RECOMMENDATION SYSTEM")
    print("=" * 60)
    
    # Initialize recommender
    recommender = MovieRecommender()
    
    # Interactive loop
    while True:
        movie_name = input("📽️  Enter a movie name (or 'quit' to exit): ").strip()
        
        if movie_name.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not movie_name:
            continue
        
        # Get recommendations
        result = recommender.get_recommendations(movie_name)
        
        if result is None:
            print(f"❌ Movie '{movie_name}' not found. Try another title.\n")
        else:
            input_movie, recommendations = result
            print(f"\n✓ Similar movies to '{input_movie}':\n")
            print(f"{'#':<3} {'Movie Title':<50} {'Similarity':<12}")
            print("-" * 65)
            
            for idx, (_, row) in enumerate(recommendations.iterrows(), 1):
                title = row['title'][:47] + "..." if len(row['title']) > 50 else row['title']
                score = f"{row['score']:.1%}"
                print(f"{idx:<3} {title:<50} {score:<12}")
            
            print()


if __name__ == "__main__":
    main()
