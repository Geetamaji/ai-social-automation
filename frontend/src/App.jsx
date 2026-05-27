import { useState, useEffect } from "react";

const [carouselImages, setCarouselImages] = useState([]);

import "./App.css";

import {

  BarChart,

  Bar,

  XAxis,

  YAxis,

  Tooltip,

  ResponsiveContainer

} from "recharts";

function App() {

  const [topic, setTopic] = useState("");

  const [template, setTemplate] = useState("Healthcare");

  const [content, setContent] = useState("");

  const [image, setImage] = useState("");

  const [history, setHistory] = useState([]);

  const [carousel, setCarousel] = useState([]);

  const [loading, setLoading] = useState(false);

  const [video, setVideo] = useState("");

  const [avatarVideo, setAvatarVideo] = useState("");

  const [scheduleTime, setScheduleTime] = useState("");

  const [audio, setAudio] = useState("");

  async function loadHistory() {

    try {

      const response = await fetch(
        "http://127.0.0.1:5003/api/history"
      );

      const data = await response.json();

      setHistory(data);

    } catch (error) {

      console.log(error);
    }
  }
  <input

  type="datetime-local"

  value={scheduleTime}

  onChange={(e) => setScheduleTime(e.target.value)}
/>

  function App() {

  const carouselImages = [
    "/img1.jpg",
    "/img2.jpg",
    "/img3.jpg"
  ];

  return (
    <div>
      {carouselImages.map((img, index) => (
        <img key={index} src={img} alt="" />
      ))}
    </div>
  );
}
const chartData = [

  {

    name: "Posts",

    value: analytics.totalPosts
  },

  {

    name: "Reels",

    value: analytics.totalReels
  },

  {

    name: "Carousel",

    value: analytics.totalCarousels
  },

  {

    name: "Downloads",

    value: analytics.totalDownloads
  }
];
import React from "react";
import "./App.css";

function App() {

  return (
    <div>Hello</div>
  );
}

export default App;
function App() {

  return (
    <div>
      <Toaster />
      Hello
    </div>
  );
}

export default App;
 useEffect(() => {

  const fetchHistory = async () => {

    try {

      const response = await fetch(
        "http://127.0.0.1:5003/api/history"
      );

      const data = await response.json();

      setHistory(data);

    } catch (error) {

      console.log(error);
    }
  };

  fetchHistory();

}, []);

  async function schedulePost() {

  try {

    const response = await fetch(

      "http://127.0.0.1:5003/schedule_post",

      {

        method: "POST",

        headers: {

          "Content-Type": "application/json"
        },

        body: JSON.stringify({

          image,

          caption: content,

          time: scheduleTime
        })
      }
    );
    const [analytics, setAnalytics] = useState({

  totalPosts: 0,

  totalReels: 0,

  totalCarousels: 0,

  totalDownloads: 0
});
    const data = await response.json();

    alert(data.message);

  } catch (error) {

    console.log(error);
  }
}
  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  const [username, setUsername] = useState("");

  const [token, setToken] = useState("");

  async function loginUser() {

  try {

    const response = await fetch(

      "http://127.0.0.1:5003/login",

      {

        method: "POST",

        headers: {

          "Content-Type": "application/json"
        },

        body: JSON.stringify({

          email,

          password
        })
      }
    );
    <div className="content-box">

  <h2>Login</h2>

  <input
    type="email"
    placeholder="Email"
    onChange={(e)=>setEmail(e.target.value)}
  />

  <br /><br />

  <input
    type="password"
    placeholder="Password"
    onChange={(e)=>setPassword(e.target.value)}
  />

  <br /><br />

  <button onClick={loginUser}>

    Login

  </button>

</div>
async function upgradePlan() {

  try {

    const response = await fetch(

      "http://127.0.0.1:5003/create-checkout-session",

      {

        method: "POST",

        headers: {

          "Content-Type": "application/json"
        },

        body: JSON.stringify({

          email
        })
      }
    );

    const data = await response.json();

    if(data.success){

      window.location.href = data.url;
    }

  } catch(error){

    console.log(error);
  }
}
<button onClick={upgradePlan}>

  Upgrade To Pro

</button>
src/pages/Success.jsx
function Success(){

  return(

    <div className="app">

      <h1>Payment Successful</h1>

    </div>
  );
}

export default Success;
function Cancel(){

  return(

    <div className="app">

      <h1>Payment Cancelled</h1>

    </div>
  );
}

export default Cancel;
src/pages/Cancel.jsx
    const data = await response.json();

    if(data.success){

      localStorage.setItem(

        "token",

        data.token
      );

      setToken(data.token);

      alert("Login Success");
    }

  } catch(error){

    console.log(error);
  }
}
  async function generatePost() {

    if (!topic) {

      alert("Please enter topic");

      return;
    }

    setLoading(true);

    try {

      const response = await fetch(

        "http://127.0.0.1:5003/generate",

        {

          method: "POST",

          headers: {

            "Content-Type": "application/json"
          },

          body: JSON.stringify({

            topic,

            template
          })
        }
      );

      <button
  onClick={schedulePost}
>
  Schedule Instagram Post
</button>

      const data = await response.json();

      if (data.success) {

        setAnalytics((prev) => ({

  ...prev,

  totalPosts: prev.totalPosts + 1,

  totalReels: prev.totalReels + 1,

  totalCarousels: prev.totalCarousels + 1
}));

        setAvatarVideo(data.avatar_video);

        setAudio(data.audio);

        setVideo(data.video);

        setContent(data.content);

        setCarouselImages(data.carousel_images);

        setImage(data.image);

        setCarousel(data.carousel);

        setCarouselImages(data.carousel_images);

        loadHistory();

      } else {

        alert("Error generating post");
      }

    } catch (error) {

      console.log(error);

      alert("Server Error");
    }

    setLoading(false);
  }

  function copyText(text) {

    navigator.clipboard.writeText(text);

    alert("Copied");
  }

  function shareWhatsApp() {

    const url =

      `https://wa.me/?text=${encodeURIComponent(content)}`;

    window.open(url, "_blank");
  }
  if (loading) {

  return (

    <div className="loading-screen">

      <div className="ai-loader"></div>

      <h1>AI Generating Content...</h1>

      <p>

        Creating captions, posters & carousel

      </p>

    </div>
  );
}

  return (

    <div className="app">

      <h1>AI Social Media Generator</h1>

      <div className="top-controls">

        <input

          type="text"

          placeholder="Enter Topic"

          value={topic}

          onChange={(e) => setTopic(e.target.value)}
        />

        <select

          value={template}

          onChange={(e) => setTemplate(e.target.value)}
        >

          <option>Healthcare</option>

          <option>Fitness</option>

          <option>Business</option>

          <option>Education</option>

          <option>Real Estate</option>

        </select>

        <button

          onClick={generatePost}

          disabled={loading}
        >

          {
  loading ? (

    <span className="loader-text">

      Generating AI...

    </span>

  ) : (

    "Generate Post"
  )
}

        </button>

      </div>

      {

        content && (

          <div className="content-box">

            <h2>Generated Content</h2>

            <pre>{content}</pre>

            <div className="button-group">

              <button
                onClick={() => copyText(content)}
              >
                Copy Content
              </button>

              <button
                onClick={shareWhatsApp}
              >
                Share WhatsApp
              </button>

            </div>

          </div>
        )
      }

      {

        image && (

          <div className="poster-section">

            <h2>Generated Poster</h2>

            <img

              src={image}

              alt="poster"

              className="poster-image"
            />

            <br />

            <a
              href={image}
              download
            >

              <button>

                Download Poster

              </button>

            </a>

          </div>
        )
      }

      {

        carousel.length > 0 && (

          <div className="carousel-section">

            <h2>AI Carousel Slides</h2>

            <div className="carousel-grid">

              {

                carousel.map((slide, index) => (

                  <div
                    key={index}
                    className="slide-card"
                  >

                    <h3>

                      Slide {index + 1}

                    </h3>

                    <h4>

                      {slide.title}

                    </h4>

                    <p>

                      {slide.text}

                    </p>

                  </div>
                ))
              }

            </div>

          </div>
        )
      }

      <div className="history-section">

        <h2>Post History</h2>

        <div className="history-grid">

          {

            history.map((post) => (

              <div

                key={post.id}

                className="history-card"
              >

                <img
                  src={post.image}
                  alt=""
                />

                <h3>

                  {post.topic}

                </h3>

                <p>

                  {post.template}

                </p>

              </div>
            ))
          }

        </div>

      </div>

    </div>
  );
}
<div className="carousel-section">

  <h2>Carousel Images</h2>

  <div className="history-grid">

    {

      carouselImages.map((img, index) => (

        <div
          key={index}
          className="history-card"
        >

          <img
            src={img}
            alt=""
          />

          <a
            href={img}
            download
          >

            <button>

              Download Slide

            </button>

          </a>

        </div>
      ))
    }

  </div>

</div>
{
  video && (

    <div className="poster-section">

      <h2>AI Reel Video</h2>

      <video

        controls

        className="poster-image"
      >

        <source
          src={video}
          type="video/mp4"
        />

      </video>

      <br />

      <a
        href={video}
        download
      >

        <button>

          Download Reel

        </button>

      </a>

    </div>
  )
}
{
  audio && (

    <div className="poster-section">

      <h2>AI Voiceover</h2>

      <audio controls>

        <source
          src={audio}
          type="audio/mp3"
        />

      </audio>

      <br /><br />

      <a
        href={audio}
        download
      >

        <button>

          Download Voice

        </button>

      </a>

    </div>
  )
}
{
  avatarVideo && (

    <div className="poster-section">

      <h2>AI Avatar Presenter</h2>

      <video
        controls
        className="poster-image"
      >

        <source
          src={avatarVideo}
          type="video/mp4"
        />

      </video>

    </div>
  )
}
<div className="analytics-section">

  <h2>Analytics Dashboard</h2>

  <div className="analytics-grid">

    <div className="analytics-card">

      <h3>Total Posts</h3>

      <h1>{analytics.totalPosts}</h1>

    </div>

    <div className="analytics-card">

      <h3>Total Reels</h3>

      <h1>{analytics.totalReels}</h1>

    </div>

    <div className="analytics-card">

      <h3>Total Carousel</h3>

      <h1>{analytics.totalCarousels}</h1>

    </div>

    <div className="analytics-card">

      <h3>Downloads</h3>

      <h1>{analytics.totalDownloads}</h1>

    </div>

  </div>

  <div className="chart-box">

    <ResponsiveContainer
      width="100%"
      height={350}
    >

      <BarChart data={chartData}>

        <XAxis dataKey="name" />

        <YAxis />

        <Tooltip />

        <Bar
          dataKey="value"
          fill="#00bfff"
        />

      </BarChart>

    </ResponsiveContainer>

  </div>

</div>
export default App;