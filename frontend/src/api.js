import axios from 'axios'
import { StoryRead, StoryCreate } from "./model.js"

export async function getStories(){
    const stories = [];

    await axios.get('http://localhost:8000/stories')
    .then((response) => {
        for(const story of response.data){
            stories.push(new StoryRead(
                story.id, story.title, story.story
            ))
        }
    });

    return stories
}

export async function putStory(title, story){
    await axios.post('http://localhost:8000/stories', new StoryCreate(title, story))
    .then((response) => {
        console.log(response.data);
    })
}