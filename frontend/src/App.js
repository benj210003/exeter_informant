import { useState, useEffect } from "react";
import {getStories, putStory} from "./api.js"
import StoryBoard from "./StoryBoard.js";
import StoryInput from "./StoryInput.js";

async function addStory (title, story) {
  await putStory(title, story);
}

function App() {

  const [stories, setStories] = useState(null);

  useEffect(() => {
    async function fetchStories () {
      const fetchedStories = await getStories();
      setStories(fetchedStories);
    }
    fetchStories();
  }, [])

  return(
    <><h1>Exeter Informant</h1>
    <StoryInput></StoryInput>
    <h1>{stories !== null ? <StoryBoard stories={stories}/> : "No Stories available"}</h1></>
  )
}

export default App;
