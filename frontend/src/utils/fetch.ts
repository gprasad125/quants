export const API_URL = import.meta.env.VITE_API_URL;

export const protectedFetch = async <T>(url: string, options: RequestInit) => {
	const res = await fetch(url, options);
	const json = await res.json();
	if (!res.ok) throw json;
	return json as T;
};
