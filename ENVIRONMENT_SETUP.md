# Environment Setup Guide

## Prerequisites

Make sure you have:
- ✅ Node.js installed (v14 or higher)
- ✅ MongoDB installed and running locally OR MongoDB Atlas account
- ✅ npm or yarn package manager

## Step-by-Step Setup

### 1. Install Dependencies
```bash
cd C:\Users\SADANAND\ai-social-automation
npm install
```

### 2. Create .env File
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### 3. Configure Environment Variables

Edit `.env` file with your settings:

```env
# Server Configuration
PORT=5000
NODE_ENV=development

# Database Configuration
# Option A: Local MongoDB (default)
MONGODB_URI=mongodb://localhost:27017/ai-social-automation

# Option B: MongoDB Atlas (cloud)
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/ai-social-automation?retryWrites=true&w=majority

# JWT Configuration
JWT_SECRET=your_super_secret_key_here_change_in_production_to_random_string
JWT_EXPIRE=7d

# Social Media API Keys (optional for now)
TWITTER_API_KEY=your_key_here
TWITTER_API_SECRET=your_secret_here
FACEBOOK_ACCESS_TOKEN=your_token_here
INSTAGRAM_ACCESS_TOKEN=your_token_here
LINKEDIN_ACCESS_TOKEN=your_token_here

# AI Services (optional for now)
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4

# Logging
LOG_LEVEL=info
```

### 4. Setup MongoDB Locally

**Option A: Local MongoDB Installation**

1. Install MongoDB Community Edition from https://www.mongodb.com/try/download/community
2. Start MongoDB:
   - Windows: `net start MongoDB` (or use MongoDB Compass GUI)
   - Or run: `mongod` in terminal

3. Verify connection:
   ```bash
   mongo mongodb://localhost:27017/ai-social-automation
   ```

**Option B: MongoDB Atlas (Cloud)**

1. Create account at https://www.mongodb.com/cloud/atlas
2. Create a cluster
3. Get connection string
4. Update `MONGODB_URI` in `.env`:
   ```
   MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/ai-social-automation?retryWrites=true&w=majority
   ```

### 5. Generate JWT Secret

For development, you can use any string. For production, generate a random string:

**Windows PowerShell:**
```powershell
[Convert]::ToBase64String([System.Security.Cryptography.RandomNumberGenerator]::GetBytes(32))
```

**Linux/Mac:**
```bash
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
```

Update `JWT_SECRET` in `.env` with the generated value.

### 6. Start Development Server

```bash
npm run dev
```

Expected output:
```
🚀 Server running on http://localhost:5000
Environment: development
Database: mongodb://localhost:27017/ai-social-automation
```

### 7. Verify Server is Running

Open browser and visit:
- **Health Check**: http://localhost:5000/health
- **API Root**: http://localhost:5000/api

### 8. Test API Endpoints

Run the automated test script:
```bash
test-api.bat
```

Or test manually with curl:

**Health Check:**
```bash
curl http://localhost:5000/health
```

**Register User:**
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "password": "TestPass123",
    "confirmPassword": "TestPass123"
  }'
```

---

## Troubleshooting

### MongoDB Connection Failed
**Error:** `MongooseServerSelectionError: connect ECONNREFUSED 127.0.0.1:27017`

**Solutions:**
1. Make sure MongoDB is running: `mongod` or `net start MongoDB`
2. Check connection string in `.env`
3. If using MongoDB Atlas, verify:
   - Cluster is active
   - IP whitelist includes your IP (or 0.0.0.0/0 for development)
   - Username and password are correct

### Port Already in Use
**Error:** `Error: listen EADDRINUSE: address already in use :::5000`

**Solution:**
- Change PORT in `.env` to another port (e.g., 5001)
- Or kill process using port 5000:
  ```bash
  netstat -ano | findstr :5000
  taskkill /PID <PID> /F
  ```

### JWT Secret Not Set
**Error:** `Error: jwt must be provided`

**Solution:**
- Ensure `JWT_SECRET` is set in `.env`
- Should be a random string (minimum 10 characters recommended)

### Dependencies Not Installing
**Error:** `npm ERR! could not find package`

**Solutions:**
1. Clear cache: `npm cache clean --force`
2. Delete `node_modules` and `package-lock.json`
3. Run `npm install` again
4. Try `npm ci` instead of `npm install`

### Node Module Issues
**Error:** `Module not found`

**Solution:**
```bash
npm install
npm run dev
```

---

## Development Tools

### VS Code Extensions (Recommended)
- REST Client - Test APIs directly in VS Code
- MongoDB for VS Code - Browse MongoDB
- Thunder Client - API testing
- Postman - Desktop API testing

### Monitor Database Changes
Use MongoDB Compass:
```bash
mongod --install
mongod --start
```

---

## Environment Variables Reference

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| PORT | Server port | 5000 | No |
| NODE_ENV | Environment mode | development | No |
| MONGODB_URI | Database connection | localhost:27017 | No |
| JWT_SECRET | JWT signing key | - | Yes |
| JWT_EXPIRE | Token expiration | 7d | No |
| LOG_LEVEL | Logging level | info | No |

---

## Production Setup

When deploying to production:

1. **Use Environment Variables**
   - Never hardcode secrets
   - Use `.env` file (not committed to git)

2. **Change JWT_SECRET**
   - Generate a strong random string
   - Store securely in environment

3. **Update MONGODB_URI**
   - Use MongoDB Atlas or managed database
   - Use connection pooling

4. **Set NODE_ENV=production**
   - Enables optimizations
   - Disables detailed error logs

5. **Enable CORS Properly**
   - Specify allowed origins
   - Don't use `*` in production

6. **Use HTTPS**
   - Install SSL certificate
   - Redirect HTTP to HTTPS

7. **Add Rate Limiting**
   - Implement request throttling
   - Protect against abuse

---

## Quick Commands

```bash
# Install dependencies
npm install

# Start development server (with hot reload)
npm run dev

# Start production server
npm start

# Run tests
npm test

# Run linter
npm run lint

# Clear node_modules and reinstall
rm -r node_modules package-lock.json && npm install
```

---

## Next Steps

1. ✅ Install and run server
2. ✅ Test all API endpoints
3. ✅ Verify database connection
4. 📝 Create frontend (React/Vue)
5. 🔌 Integrate social media APIs
6. 🤖 Add AI features
7. 🚀 Deploy to production

---

## Support Resources

- **Express.js**: https://expressjs.com/
- **Mongoose**: https://mongoosejs.com/
- **JWT**: https://jwt.io/
- **MongoDB**: https://docs.mongodb.com/
- **Node.js**: https://nodejs.org/en/docs/

Happy coding! 🎉
