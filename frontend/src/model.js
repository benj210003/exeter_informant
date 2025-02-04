class StoryRead{
    constructor(id, title, story){
        this.id = id;
        this.title = title;
        this.story = story;
    }
}

class StoryCreate{
    constructor(title, story){
        this.title = title;
        this.story = story;
    }
}

export {StoryRead, StoryCreate};