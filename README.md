# Pastebin API

A Django REST Framework API for creating and sharing text snippets — similar to pastebin.com. Users can create pastes with optional expiration and privacy settings, and retrieve them either as structured JSON or raw plain text.

## Features

- **Create, read, update, and delete pastes** via a REST API
- **Auto-generated short slugs** for each paste (e.g. `aB3xQ2`) — no client-side ID needed
- **Expiration** — pastes can be given an optional expiry time, after which they're no longer accessible
- **Public/private visibility** — pastes can be marked private, restricting access to the owner only
- **Ownership & permissions** — only the paste's owner can edit or delete it; public pastes are readable by anyone
- **Raw text endpoint** — retrieve a paste's content as plain text (`text/plain`), separate from the JSON API, for direct use in terminals, scripts, or browsers
- **Token authentication** — requests are authenticated via DRF's token auth to identify the requesting user

## Tech Stack

- Python / Django
- Django REST Framework
- Token Authentication (`rest_framework.authtoken`)
- SQLite (development)

## API Overview

| Endpoint | Method | Description |
|---|---|---|
| `/api/pastes/` | GET | List all pastes visible to the requester |
| `/api/pastes/` | POST | Create a new paste |
| `/api/pastes/<slug>/` | GET | Retrieve a single paste (JSON) |
| `/api/pastes/<slug>/` | PATCH | Update a paste (owner only) |
| `/api/pastes/<slug>/` | DELETE | Delete a paste (owner only) |
| `/paste/<slug>/raw/` | GET | Retrieve a paste's raw text content |

## Setup

```bash
git clone https://github.com/Afnan-Shahid3/pastebin-api.git
cd pastebin-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Authentication

Requests that create, edit, or access private pastes require a token, sent via header

## Notes

This project was built as a learning exercise to practice Django REST Framework concepts beyond basic CRUD — including custom permissions, conditional visibility logic, and mixing plain Django views with DRF views in the same project.