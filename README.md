# Http-methods-poc

## Author

**Abhilakshay Singh Pathania**

GitHub: lakshay-08 (https://github.com/lakshay-08)

This is a POC on varioud types of http methods that can be made for a better understanding of working of it.


HTTP (Hypertext Transfer Protocol) is the backbone of web communication. As developers, understanding the core request methods is essential for building robust APIs, optimizing client-server interactions, and debugging issues effectively. Here's a quick overview of the 9 HTTP methods you should master:

1. GET
Used to retrieve data from the server. It’s safe, idempotent, and doesn’t modify server resources.
Example: Fetching a list of users.

GET /users

2. POST
Used to create new resources or submit data to the server. Unlike GET, it modifies server state.
Example: Adding a new user.

POST /users

3. PUT
Used to update or replace an entire resource on the server. Typically idempotent.
Example: Updating a user’s profile.

PUT /users/123

4. PATCH
Used to partially update a resource. It’s ideal for making incremental changes.
Example: Changing a user’s email address.

PATCH /users/123

5. DELETE
Used to remove a resource from the server. Like GET, it’s idempotent.
Example: Deleting a specific user.

DELETE /users/123

6. HEAD
Similar to GET, but only fetches the headers (no response body). Useful for checking if a resource exists or for caching validation.
Example: Checking resource metadata.

HEAD /users/123

7. OPTIONS
Used to discover available methods and CORS policies for a specific resource. It’s helpful during API exploration and debugging.
Example: Checking what actions are allowed.
OPTIONS /users

8. CONNECT
Establishes a tunnel to the server (usually for SSL/HTTPS communication). Used by proxies and rarely in day-to-day API development.

9. TRACE
Performs a loopback test to debug connection issues by returning what the server receives. Use with caution due to security concerns.

Why These Methods Matter
Each HTTP method has a specific purpose and behavior, helping developers create intuitive, predictable, and RESTful APIs. Misusing them can lead to performance issues, security vulnerabilities, or confusion for clients consuming your API.



# headers to be added

1. **Content-Security-Policy**: default-src 'self' (Defines allowed content sources).
2. **Strict-Transport-Security**: max-age=31536000; includeSubDomains; preload (Enforces HTTPS).
3. **X-Content-Type-Options**: nosniff (Prevents MIME-type sniffing).
4. **X-Frame-Options**: DENY (Blocks clickjacking).
5. **X-XSS-Protection**: 1; mode=block (Enables XSS protection).
6. **Access-Control-Allow-Origin**: * (Allows cross-origin requests).
7. **Referrer-Policy**: no-referrer (Restricts referrer data).
8. **Permissions-Policy**: geolocation=(), microphone=() (Limits browser API access).
9. **Cache-Control**: no-cache, no-store, must-revalidate (Controls caching).
10. **Expires**: 0 (Sets resource expiration).
11. **ETag**: abc123 (Uniquely identifies the resource).
12. **Last-Modified**: Wed, 21 Dec 2023 10:45:00 GMT (Indicates last update).
13. **Content-Type**: application/json; charset=utf-8 (Defines media type).
14. **Content-Disposition**: inline (Specifies content handling).
15. **Accept-Ranges**: bytes (Supports partial downloads).
16. **RateLimit-Limit**: 100 (Sets request limit).
17. **RateLimit-Remaining**: 50 (Shows remaining requests).
18. **RateLimit-Reset**: 3600 (Time until rate limit resets).
19. **Server**: secure-api-server (Hides server details).
20. **Date**: Wed, 21 Dec 2023 10:45:00 GMT (Response timestamp).
21. **Connection**: keep-alive (Specifies connection behavior).
22. **Vary**: Accept-Encoding (Improves caching behavior).
