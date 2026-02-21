# Technical Specs

## Business Goal:
A language learning school wants to build a prototype of learning portal which will act as three things:
- Inventory of possible vocabulary that can be learned
Act as a Learning record store (LS), providing correct and wrong score on practice vocabulary
- A unified launchpad to launch different learning apps

## Technical Requirements
  - The backend will be built using Django
  - The database will be SQLite3
  - The API will be built using Gin
  - The API will always return JSON
  - There will no authentication or authorisation
  - Everthing be as a single user


## Directory Structure



## Database Schema

Our database will be a sinle sqlite database called `words.db` that will be in the root of the project folder of `backend-jango`

we have the following tables:

words - stored vocabulary words
  - id integer
  - japasese string
  - romaji string
  - english string
  - parts json

words _groups - join table for words and groups many-to-many
  - id integer
  - word_id integer
  - group-id integer

groups - thematic groups of words
  - id integer
  - name string

study_sessions - records of study sessions grouping
word_review_items
  - id integer
  - group_id integer
  - created_at datetime
  - study_activity_id integer

study_activities - a specific study activity, linking a study session to group
  - id integer
  - study_session_id integer
  - group_id integer
  - created_at datetime

word review_items - a record of word practice, determining if the word was correct or not
  - word_id integer
  - study_session_ id integer
  - correct boolean
  - created_at datetime


## API Endpoints

### GET /api/dashboard/last_study_session
```json
{
  "id": 123,
  "group_id": 5,
  "study_activity_id": 42,
  "created_at": "2026-02-20T15:32:10Z",
  "word_review_items": [
    { "word_id": 1001, "kanji": "払う", "romaji": "harau", "english": "to pay", "correct": true },
    { "word_id": 1002, "kanji": "食べる", "romaji": "taberu", "english": "to eat", "correct": false }
  ],
  "summary": { "total_attempted": 10, "correct_count": 8, "accuracy_percent": 80.0 }
}
```

### GET /api/dashboard/study_progress
```json
{
  "total_sessions": 27,
  "total_words_practiced": 542,
  "overall_accuracy_percent": 76.8,
  "streak_days": 5,
  "by_group": [
    { "group_id": 5, "group_name": "Basic Verbs", "sessions": 12, "words_practiced": 240, "accuracy_percent": 81.3 }
  ]
}
```

### GET /api/dashboard/quick-stats
```json
{
  "today_sessions": 1,
  "today_correct": 8,
  "today_incorrect": 2,
  "next_review_count": 18
}
```

### GET /api/study-activities/:id
```json
{
  "id": 42,
  "group_id": 5,
  "created_at": "2026-02-20T15:00:00Z",
  "description": "Timed practice - verbs",
  "study_sessions_count": 3
}
```

### GET /api/study-activities/:id/study_sessions
```json
[
  { "id": 120, "created_at": "2026-02-20T15:30:00Z", "accuracy_percent": 80.0 },
  { "id": 121, "created_at": "2026-02-18T12:10:00Z", "accuracy_percent": 75.0 }
]
```

### POST /api/study_activites
required params: group_id , study_activity_id
```json
{
  "id": 99,
  "group_id": 5,
  "study_activity_id": 42,
  "created_at": "2026-02-21T10:00:00Z",
  "message": "study activity created"
}
```

### GET /api/words
### pagination with 100 items per page
```json
{
  "page": 1,
  "per_page": 100,
  "total": 542,
  "items": [
    { "id": 1001, "kanji": "払う", "romaji": "harau", "english": "to pay" },
    { "id": 1002, "kanji": "食べる", "romaji": "taberu", "english": "to eat" }
  ]
}
```

### GET /api/words/:id
```json
{
  "id": 1001,
  "kanji": "払う",
  "romaji": "harau",
  "english": "to pay",
  "parts": [{ "kanji": "払", "romaji": ["ha","ra"] }, { "kanji": "う", "romaji": ["u"] }]
}
```

### GET /api/groups
```json
{
  "groups": [
    { "id": 5, "name": "Basic Verbs", "words_count": 240 },
    { "id": 7, "name": "Adjectives", "words_count": 160 }
  ]
}
```

### GET /api/groups/:id
### pagination with 100 items per page
```json
{
  "id": 5,
  "name": "Basic Verbs",
  "description": "Common verb forms",
  "words_count": 240
}
```

### GET /api/groups/:id/words
```json
{
  "group_id": 5,
  "page": 1,
  "per_page": 100,
  "items": [ { "id": 1001, "kanji": "払う", "romaji": "harau", "english": "to pay" } ]
}
```

### GET /api/groups/:id/study sessions
```json
[
  { "id": 120, "created_at": "2026-02-20T15:30:00Z", "accuracy_percent": 80.0 },
  { "id": 110, "created_at": "2026-02-18T09:00:00Z", "accuracy_percent": 72.5 }
]
```

### GET /api/study_sessions
### pagination with 100 items per page
```json
{
  "page": 1,
  "per_page": 100,
  "total": 27,
  "items": [ { "id": 120, "group_id": 5, "created_at": "2026-02-20T15:30:00Z" } ]
}
```

### GET /api/study_sessions/:id
```json
{
  "id": 120,
  "group_id": 5,
  "created_at": "2026-02-20T15:30:00Z",
  "word_review_items": [ { "word_id": 1001, "correct": true }, { "word_id": 1002, "correct": false } ]
}
```

### GET /api/study_sessions/:id/words
```json
{
  "study_session_id": 120,
  "words": [ { "id": 1001, "kanji": "払う", "romaji": "harau", "english": "to pay" } ]
}
```

### POST /api/reset history
```json
{ "status": "ok", "message": "history reset" }
```

### POST /api/full reset
```json
{ "status": "ok", "message": "full reset completed" }
```

### POST /api/study_ses:correct
```json
{
  "study_session_id": 120,
  "word_id": 1002,
  "correct": true,
  "updated_at": "2026-02-21T10:05:00Z"
}
```


## Tasks
This is a task runner for Django. Lets list out possible tasks we need for our lang portal

### Initialise Database 
Task will initialise the sqlite database called `word.db`.

### Migrate Database
This task will run a series of migrations sqlfiles on the database.

### Seed Data

This task will import json files and transform them into target data for our database.
All seed files should be loaded
All seed files should be loaded

In our task we should have DSL to specific each seed file and its expected group word name. 


```json 
  {
    "kanji": "払う",
    "romaji": "harau",
    "english": "to pay",
    "parts": [
      { "kanji": "払", "romaji": ["ha","ra"] },
      { "kanji": "う", "romaji": ["u"] }
    ]
  },
```







