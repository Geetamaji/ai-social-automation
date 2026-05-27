import React, { useState } from "react"
// ====================================
// STATES
// ====================================

const [topic, setTopic] = useState("");
const [template, setTemplate] = useState("healthcare");
const [loading, setLoading] = useState(false);
const [posts, setPosts] = useState([]);

// ====================================
// FETCH POSTS
// ====================================

async function fetchPosts() {}
  try {
    const response = await fetch(
      "http://127.0.0.1:5003/api/ai/generate",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          topic: topic,
          template: template,
        }),
      }
    );

    const data = await response.json();

    console.log(data);

    } catch (error) {
    console.log(error);
  }
}