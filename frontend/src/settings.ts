export const API_URL = import.meta.env.MODE === 'production' ? 'wss://notionqa.sillyslime.dev/ask' : 'ws://localhost:8000/ask';

export const DEV_URL = "http://localhost:8000/ask/"
export const FILE_URL = "http://localhost:8000/upload/"
export const INGEST_URL = "http://localhost:8000/ingest/"
