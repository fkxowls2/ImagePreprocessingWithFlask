function uploadImage() {
    const fileInput = document.getElementById("myFile");
    const uploadedImage = document.getElementById("uploadedImage");
    
    // 파일을 선택하지 않은 경우
    if (!fileInput.value) {
        return;
    }
    
    const file = fileInput.files[0];
    const reader = new FileReader();
    
    // 파일을 읽은 후 이미지를 표시
    reader.onload = function() {
      uploadedImage.src = reader.result;
    }
    
    // 이미지 파일 읽기 시작
    reader.readAsDataURL(file);
}

function reloadImage() {
  var imgElement = document.getElementById("preprocessingImage");
  var src = imgElement.getAttribute("src");
  // 매개변수를 추가하여 URL을 변경합니다.
  //src = src + "?time=" + new Date().getTime();
  src = src + "?1"
  imgElement.setAttribute("src", src);
}

function slide_event() {
  var slider = document.getElementById("slider");
  var sliderValue = document.getElementById("sliderValue");
  sliderValue.innerHTML = slider.value;
  
  slider.oninput = function() {
      sliderValue.innerHTML = this.value;
  }
}

function slide_event_handler() {
  // 슬라이더 이벤트 핸들러 등록
  document.getElementById("slider").addEventListener("input", function() {
    // 서버로 슬라이더 값을 전송
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/slide_binary", true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send("value=" + this.value);
    // 서버에서 반환한 이미지 업데이트
    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            //document.getElementById("result").src = "data:image/jpeg;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(this.response)));
            reloadImage();
        }
    }
    // 슬라이더 값을 출력
    document.getElementById("sliderValue").innerHTML = this.value;
  });
}

function hidden_slide() {
  document.getElementById("slideSector").style.display = "none";
}