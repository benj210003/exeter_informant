export default function StoryBoard({stories}) {
    return (
      <ul>
        {stories.map((story) => (
          <li key={story.id}>
            <h1>{story.title}</h1>
            <p>{story.story}</p>
          </li>
        ))}
      </ul>
    );
}