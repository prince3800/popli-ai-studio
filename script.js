const imageUpload = document.getElementById('imageUpload');
const generateBtn = document.getElementById('generateBtn');
const videoContainer = document.getElementById('videoContainer');

generateBtn.addEventListener('click', () => {
    if (imageUpload.files.length === 0) {
        alert('Please upload an image first!');
        return;
    }

    const file = imageUpload.files[0];
    const reader = new FileReader();
    
    reader.onload = function(e) {
        const imgElement = document.createElement('img');
        imgElement.src = e.target.result;
        imgElement.style.width = '200px';
        imgElement.style.height = 'auto';
        imgElement.style.margin = '10px';
        videoContainer.innerHTML = '';
        videoContainer.appendChild(imgElement);

        // Simulate video generation
        setTimeout(() => {
            const video = document.createElement('video');
            video.src = "sample-video.mp4"; // Replace with generated video later
            video.controls = true;
            video.width = 300;
            videoContainer.innerHTML = '';
            videoContainer.appendChild(video);
        }, 3000); // 3 sec simulation
    };

    reader.readAsDataURL(file);
});
