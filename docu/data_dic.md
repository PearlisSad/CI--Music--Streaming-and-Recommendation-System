# Spotify Tracks Data Dictionary

Complete data dictionary for Spotify tracks dataset columns, including identifiers, metadata, popularity metrics, and audio features from Spotify's API. Useful for ML modeling, genre classification, and music analytics projects.

## Column Specifications

| Column             | Type              | Description |
|--------------------|-------------------|-------------|
| track_id          | String           | Unique Spotify ID for the track (e.g., "spotify:track:2takcwOaAZWiXQijPHIx7B"). |
| artists           | String           | Names of performing artists, separated by semicolons for multiples. |
| album_name        | String           | Name of the album containing the track. |
| track_name        | String           | Title of the track. |
| popularity        | Integer (0-100)  | Score where higher values indicate greater popularity based on plays and recency. |
| duration_ms       | Integer          | Track length in milliseconds. |
| explicit          | Boolean          | Indicates if the track contains explicit lyrics. |
| danceability      | Float (0.0-1.0)  | Suitability for dancing based on tempo, rhythm stability, beat strength, and regularity (0.0 least, 1.0 most). |
| energy            | Float (0.0-1.0)  | Perceived intensity and activity (0.0 calm, 1.0 high-energy). |
| key               | Integer (-1 to 11)| Numeric key (0=C, 1=C♯/D♭); -1 if no key detected. |
| loudness          | Float            | Overall loudness in decibels (typically -60 to 0). |
| mode              | Integer (0-1)    | Modality (0=major, 1=minor). |
| speechiness       | Float (0.0-1.0)  | Presence of spoken words (0.0=music, 1.0=spoken like podcast). |
| acousticness      | Float (0.0-1.0)  | Confidence that the track is acoustic (0.0=electric, 1.0=acoustic). |
| instrumentalness  | Float (0.0-1.0)  | Likelihood of no vocals (0.0=vocalic, 1.0=instrumental). |
| liveness          | Float (0.0-1.0)  | Detection of live audience (higher for live recordings). |
| valence           | Float (0.0-1.0)  | Musical positiveness (0.0=sad/angry, 1.0=happy/cheerful). |
| tempo             | Float            | Estimated beats per minute (BPM). |
| time_signature    | Integer          | An estimated overall time signature (e.g., 4/4 as 4). |
| track_genre       | String           | Assigned genre label (e.g., from datasets covering 125 genres). |