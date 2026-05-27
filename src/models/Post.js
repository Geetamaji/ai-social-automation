const mongoose = require('mongoose');

const postSchema = new mongoose.Schema(
  {
    title: {
      type: String,
      required: [true, 'Post title is required'],
      trim: true,
    },

    content: {
      type: String,
      required: [true, 'Post content is required'],
      trim: true,
    },

    platform: {
      type: String,
      required: [true, 'Platform is required'],
      enum: ['twitter', 'linkedin', 'facebook', 'instagram', 'youtube', 'other'],
      lowercase: true,
      trim: true,
    },

    status: {
      type: String,
      enum: ['draft', 'scheduled', 'published', 'failed'],
      default: 'draft',
      lowercase: true,
      trim: true,
    },

    scheduledAt: {
      type: Date,
      default: null,
    },

    publishedAt: {
      type: Date,
      default: null,
    },

    author: {
      type: mongoose.Schema.Types.ObjectId,
      ref: 'User',
      required: true,
    },
  },
  {
    timestamps: true,
  }
);

module.exports = mongoose.model('Post', postSchema);