const Post = require('../models/Post');

// Helper: token se user id nikalne ke liye
const getUserId = (req) => {
  return req.user?.id || req.user?.userId || req.user?._id;
};

// @desc    Create new post
// @route   POST /api/posts
// @access  Private
exports.createPost = async (req, res) => {
  try {
    const { title, content, platform, status, scheduledFor } = req.body;

    const authorId = getUserId(req);

    if (!authorId) {
      return res.status(401).json({
        success: false,
        message: 'Unauthorized: user id not found in token'
      });
    }

    const post = await Post.create({
      title,
      content,
      platform,
      status,
      scheduledFor,
      author: authorId
    });

    res.status(201).json({
      success: true,
      message: 'Post created successfully',
      data: post
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to create post',
      error: error.message
    });
  }
};

// @desc    Get all posts of logged in user
// @route   GET /api/posts
// @access  Private
exports.getPosts = async (req, res) => {
  try {
    const authorId = getUserId(req);

    if (!authorId) {
      return res.status(401).json({
        success: false,
        message: 'Unauthorized: user id not found in token'
      });
    }

    const posts = await Post.find({ author: authorId }).sort({ createdAt: -1 });

    res.status(200).json({
      success: true,
      message: 'Posts fetched successfully',
      count: posts.length,
      data: posts
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to fetch posts',
      error: error.message
    });
  }
};

// @desc    Get my posts
// @route   GET /api/posts/my-posts
// @access  Private
exports.getMyPosts = async (req, res) => {
  try {
    const authorId = getUserId(req);

    if (!authorId) {
      return res.status(401).json({
        success: false,
        message: 'Unauthorized: user id not found in token'
      });
    }

    const posts = await Post.find({ author: authorId }).sort({ createdAt: -1 });

    res.status(200).json({
      success: true,
      message: 'My posts fetched successfully',
      count: posts.length,
      data: posts
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to fetch my posts',
      error: error.message
    });
  }
};

// @desc    Get single post by id
// @route   GET /api/posts/:id
// @access  Private
exports.getPostById = async (req, res) => {
  try {
    const authorId = getUserId(req);

    if (!authorId) {
      return res.status(401).json({
        success: false,
        message: 'Unauthorized: user id not found in token'
      });
    }

    const post = await Post.findOne({
      _id: req.params.id,
      author: authorId
    });

    if (!post) {
      return res.status(404).json({
        success: false,
        message: 'Post not found'
      });
    }

    res.status(200).json({
      success: true,
      message: 'Post fetched successfully',
      data: post
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to fetch post',
      error: error.message
    });
  }
};

// @desc    Update post
// @route   PUT /api/posts/:id
// @access  Private
exports.updatePost = async (req, res) => {
  try {
    const authorId = getUserId(req);

    if (!authorId) {
      return res.status(401).json({
        success: false,
        message: 'Unauthorized: user id not found in token'
      });
    }

    const { title, content, platform, status, scheduledFor } = req.body;

    const post = await Post.findOneAndUpdate(
      {
        _id: req.params.id,
        author: authorId
      },
      {
        title,
        content,
        platform,
        status,
        scheduledFor
      },
      {
        new: true,
        runValidators: true
      }
    );

    if (!post) {
      return res.status(404).json({
        success: false,
        message: 'Post not found'
      });
    }

    res.status(200).json({
      success: true,
      message: 'Post updated successfully',
      data: post
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to update post',
      error: error.message
    });
  }
};

// @desc    Delete post
// @route   DELETE /api/posts/:id
// @access  Private
exports.deletePost = async (req, res) => {
  try {
    const authorId = getUserId(req);

    if (!authorId) {
      return res.status(401).json({
        success: false,
        message: 'Unauthorized: user id not found in token'
      });
    }

    const post = await Post.findOneAndDelete({
      _id: req.params.id,
      author: authorId
    });

    if (!post) {
      return res.status(404).json({
        success: false,
        message: 'Post not found'
      });
    }

    res.status(200).json({
      success: true,
      message: 'Post deleted successfully',
      data: post
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: 'Failed to delete post',
      error: error.message
    });
  }
};