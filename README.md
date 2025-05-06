#  Orikari Backend
Backend for Orikari project made with FastAPI + Supabase.

## Table of Contents
- [Orikari Backend](#orikari-backend)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)

## Installation

1. Clone the repo:

```bash
git clone https://github.com/ElJako11/Orikari-Backend.git
cd Orikari-Backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```env
SUPABASE_URL="project_url"
SUPABASE_KEY="api_key"
```

## Usage

Run the uvicorn server:

```bash
cd src
uvicorn main:app --reload
```

## License
This project is under the MIT License. See LICENSE for more details.