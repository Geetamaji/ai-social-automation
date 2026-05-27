const express = require('express');
const router = express.Router();

const postController = require('../controllers/postController');
const authMiddleware = require('../middleware/auth');

// Create post
router.post('/', authMiddleware, postController.createPost);

// Get all posts
router.get('/', authMiddleware, postController.getPosts);

// IMPORTANT:
// my-posts ko /:id se pehle rakhna zaroori hai.
// Warna Express "my-posts" ko id samajh lega.
router.get('/my-posts', authMiddleware, postController.getMyPosts);

// ID routes hamesha static routes ke baad
router.get('/:id', authMiddleware, postController.getPostById);
router.put('/:id', authMiddleware, postController.updatePost);
router.delete('/:id', authMiddleware, postController.deletePost);

module.exports = router;