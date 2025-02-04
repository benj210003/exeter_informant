import {putStory} from "./api.js";

async function addStory (e) {
    e.preventDefault()
    
    const form = e.target;
    const formData = new FormData(form)
    const formJson = Object.fromEntries(formData.entries())
    // console.log(formJson["title"] + formJson["story"]);
    
    await putStory(formJson["title"], formJson["story"]);
}

export default function StoryInput() {
    return (<>
    <form method="post" onSubmit={addStory}>
      <label>
        Title: <input name="title"></input>
      </label>
      <br/>
      <label>
        Story: <input name="story"></input>
      </label>
      <br/>
      <button type="submit">Submit story</button>
    </form>
    </>);
}