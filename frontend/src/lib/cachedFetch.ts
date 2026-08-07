export const apiCache = new Map<string, { data: any; timestamp: number }>();

const DEFAULT_TTL_MS = 60 * 1000; // 1 minute default TTL for global GET requests

/**
 * A wrapper around the native browser `fetch` that caches GET request responses in memory.
 * Helps prevent redundant backend API calls during rapid component re-renders or navigation.
 */
export async function cachedFetch(url: string | URL | Request, options?: RequestInit & { ttl?: number }): Promise<Response> {
    const urlStr = url.toString();
    const method = options?.method?.toUpperCase() || "GET";

    // Only cache GET requests
    if (method !== "GET") {
        return fetch(url, options);
    }

    const ttl = options?.ttl ?? DEFAULT_TTL_MS;
    const now = Date.now();
    const cached = apiCache.get(urlStr);

    if (cached && (now - cached.timestamp < ttl)) {
        // Return a mock Response object with the cached JSON
        return new Response(JSON.stringify(cached.data), {
            status: 200,
            statusText: "OK",
            headers: {
                "Content-Type": "application/json",
                "X-Cache": "HIT"
            }
        });
    }

    const response = await fetch(url, options);

    if (response.ok) {
        // Clone the response to read the body into the cache
        const clone = response.clone();
        try {
            const data = await clone.json();
            apiCache.set(urlStr, { data, timestamp: now });
        } catch (err) {
            // If it's not JSON or fails to parse, just ignore caching
        }
    }

    return response;
}

export function clearApiCache(urlPattern?: string) {
    if (!urlPattern) {
        apiCache.clear();
        return;
    }
    for (const key of apiCache.keys()) {
        if (key.includes(urlPattern)) {
            apiCache.delete(key);
        }
    }
}
