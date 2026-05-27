# MongoDB Configuration Module

## Overview

The `src/config/db.js` module handles all MongoDB database connections and disconnections for the application.

## File Location
```
src/config/db.js
```

## Features

✅ **Connection Management**
- Reads MONGODB_URI from environment variables (.env)
- Provides connection and disconnection functions
- Error handling with process exit on failure

✅ **Configuration Options**
- Uses Mongoose native URL parser
- Enables unified topology
- Automatic retry logic

✅ **Logging**
- Connection success messages
- Database name extraction and display
- Error reporting with exit codes

## Usage

### In server.js
```javascript
const { connectDB, disconnectDB } = require('./config/db');

// Connect on startup
connectDB();

// Disconnect on shutdown
process.on('SIGTERM', async () => {
  await disconnectDB();
  process.exit(0);
});
```

## Environment Variables

The module requires the following environment variable in `.env`:

```env
MONGODB_URI=mongodb://localhost:27017/ai-social-automation
```

**For MongoDB Atlas (Cloud):**
```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/ai-social-automation?retryWrites=true&w=majority
```

## Functions

### connectDB()
Connects to MongoDB using the MONGODB_URI from environment variables.

**Returns:** mongoose.connection object

**Throws:** 
- Error if MONGODB_URI is not set
- Error if connection fails
- Exits process with code 1 on failure

**Example:**
```javascript
const { connectDB } = require('./config/db');
await connectDB();
```

### disconnectDB()
Gracefully disconnects from MongoDB.

**Returns:** void (Promise)

**Throws:** Error if disconnection fails (exits process)

**Example:**
```javascript
const { disconnectDB } = require('./config/db');
await disconnectDB();
```

## Error Handling

The module includes comprehensive error handling:

1. **Missing MONGODB_URI**
   - Throws: "MONGODB_URI environment variable is not set"
   - Exit code: 1

2. **Connection Failure**
   - Logs: "❌ MongoDB connection error"
   - Exit code: 1

3. **Disconnection Failure**
   - Logs: "❌ MongoDB disconnection error"
   - Exit code: 1

## Benefits of Separate Config

✅ **Separation of Concerns**
- Database logic separate from server logic
- Cleaner, more maintainable code

✅ **Reusability**
- Can be imported in other modules
- Consistent connection handling

✅ **Testing**
- Easier to mock in tests
- Can be called independently

✅ **Scalability**
- Easy to add connection pooling
- Simple to adjust retry logic
- Clear configuration point

## Connection Flow

```
1. server.js loads .env variables
2. server.js imports { connectDB, disconnectDB }
3. server.js calls connectDB()
4. connectDB() reads MONGODB_URI from environment
5. connectDB() connects to MongoDB
6. Connection established or process exits
7. On shutdown: disconnectDB() gracefully closes connection
```

## Monitoring Connection

Check MongoDB connection status:

```javascript
const mongoose = require('mongoose');

// During runtime
if (mongoose.connection.readyState === 1) {
  console.log('MongoDB is connected');
} else {
  console.log('MongoDB is not connected');
}
```

Connection states:
- 0: Disconnected
- 1: Connected
- 2: Connecting
- 3: Disconnecting

## Example Integration

### In server.js
```javascript
require('dotenv').config();
const { connectDB, disconnectDB } = require('./config/db');

// Connect to database on startup
connectDB();

// ... rest of server code ...

// Handle graceful shutdown
process.on('SIGTERM', async () => {
  console.log('SIGTERM received, closing connections...');
  await disconnectDB();
  process.exit(0);
});

process.on('SIGINT', async () => {
  console.log('SIGINT received, closing connections...');
  await disconnectDB();
  process.exit(0);
});
```

## Troubleshooting

### "MONGODB_URI environment variable is not set"
**Solution:** Add MONGODB_URI to .env file

```env
MONGODB_URI=mongodb://localhost:27017/ai-social-automation
```

### Connection timeout
**Solution:** 
- Verify MongoDB is running
- Check connection string
- Verify network connectivity

### Authentication failed
**Solution:**
- Verify username and password (MongoDB Atlas)
- Check IP whitelist (MongoDB Atlas)
- Verify connection string format

## Performance Tips

1. **Connection Pooling**
   - Default pool size: 10
   - Adjust if needed in mongoose options

2. **Connection Timeout**
   - Currently uses default (5000ms)
   - Can be customized in connectDB options

3. **Retry Logic**
   - Consider adding retry mechanism for production
   - Implement exponential backoff

## Future Enhancements

- [ ] Add connection pooling configuration
- [ ] Implement retry logic with backoff
- [ ] Add health check endpoint
- [ ] Add metrics/monitoring
- [ ] Add connection event listeners
- [ ] Add graceful shutdown hooks
