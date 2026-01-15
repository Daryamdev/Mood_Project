
function createNote() {
  const note = document.createElement("div");
  note.classList.add("note");
  note.textContent = "🎵";
  note.style.left = Math.random() * 100 + "vw";
  document.body.appendChild(note);

  setTimeout(() => {
    note.remove();
  }, 8000);
}

setInterval(createNote, 400);

// Кнопки
const buttons = document.querySelectorAll("button");
const songList=document.getElementById("songList");

buttons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const mood = btn.getAttribute("data-mood");
    getSongsByMood(mood);
  });
});

const moodIndexes={};
async function getSongsByMood(mood) {
    try {
        const response = await fetch(`http://127.0.0.1:8000/get_songs/${mood}`);
        const data = await response.json();
        console.log(data);

        const songList = document.getElementById("songList");
        songList.innerHTML = "";

        if (data.songs.length > 0) {
            
            const randomIndex = Math.floor(Math.random() * data.songs.length);
            const song = data.songs[randomIndex];

            const li = document.createElement("li");
            li.innerHTML = `
                <p class="text-lg">${song.title} — ${song.artist}</p>
                <a href="${song.spotify}" target="_blank" class="text-teal-300 underline">Listen</a>
            `;
            songList.appendChild(li);
        } else {
            songList.innerHTML = "<p>No songs found for this mood.</p>";
        }
    } catch (error) {
        console.error("Error fetching songs:", error);
    }
}

