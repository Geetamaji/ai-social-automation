# API Documentation

## Base URL
```
http://localhost:5000/api
```

## Authentication

### Register
- **POST** `/auth/register`
- **Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "password123",
    "confirmPassword": "password123"
  }
  ```
- **Response:** Returns JWT token and user data

### Login
- **POST** `/auth/login`
- **Body:**
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- **Response:** Returns JWT token and user data

### Get Current User
- **GET** `/auth/me`
- **Headers:** `Authorization: Bearer <token>`
- **Response:** Returns current user data

### Logout
- **POST** `/auth/logout`
- **Headers:** `Authorization: Bearer <token>`
- **Response:** Logout confirmation

---

## Posts Management

All post endpoints require authentication. Include token in header:
```
Authorization: Bearer <your_jwt_token>
```

### Get All Posts
- **GET** `/posts`
- **Query Parameters:**
  - `status` (optional): 'draft', 'scheduled', 'published', 'failed'
  - `platform` (optional): 'twitter', 'facebook', 'instagram', 'linkedin'
- **Response:** Array of posts

### Create Post
- **POST** `/posts`
- **Body:**
  ```json
  {
    "content": "This is my first post!",
    "images": ["url1", "url2"],
    "platforms": ["twitter", "facebook"],
    "scheduledFor": "2026-05-20T10:00:00Z"
  }
  ```
- **Response:** Created post object

### Get Single Post
- **GET** `/posts/:id`
- **Response:** Post object

### Update Post
- **PUT** `/posts/:id`
- **Body:** Same as create (partial updates allowed)
- **Response:** Updated post object

### Delete Post
- **DELETE** `/posts/:id`
- **Response:** Deletion confirmation

### Publish Post
- **POST** `/posts/:id/publish`
- **Response:** Published post object

---

## Error Responses

All errors follow this format:
```json
{
  "success": false,
  "message": "Error message",
  "errors": []
}
```

### HTTP Status Codes
- `200` - Success
- `201` - Created
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `409` - Conflict (e.g., email already exists)
- `500` - Internal Server Error
