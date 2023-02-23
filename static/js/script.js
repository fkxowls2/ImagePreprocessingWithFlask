function reload_image(elementId) {
  const imgElement = document.getElementById(elementId);
  let src = imgElement.getAttribute("src");
  // 매개변수를 추가하여 URL을 변경합니다.
  //src = src + "?time=" + new Date().getTime();
  src = src + "?1"
  imgElement.setAttribute("src", src);
}

function load_original_image() {
    // 서버로 슬라이더 값을 전송
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/load_original", true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send("value=" + this.value);
    // 서버에서 반환한 이미지 업데이트
    xhr.onreadystatechange = function() {
      if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        reload_image("originalImage");
        reload_image("preprocessingImage");
      }
  }
}

function slide_event() {
  const slider = document.getElementById("slider");
  let sliderValue = document.getElementById("sliderValue");
  sliderValue.innerHTML = slider.value;
  
  slider.oninput = function() {
      sliderValue.innerHTML = this.value;
  }
}

function binary_slide_event() {
  // 슬라이더 이벤트 핸들러 등록
  document.getElementById("slider").addEventListener("input", function() {
    // 서버로 슬라이더 값을 전송
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/slide_binary", true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send("value=" + this.value);
    // 서버에서 반환한 이미지 업데이트
    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
          reload_image("preprocessingImage");
        }
    }
    // 슬라이더 값을 출력
    document.getElementById("sliderValue").innerHTML = this.value;
  });
}

function adthreshold_slide_event() {
  // 슬라이더 이벤트 핸들러 등록
  document.getElementById("slider").addEventListener("input", function() {
    // 서버로 슬라이더 값을 전송
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/slide_adthreshold", true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send("value=" + this.value);
    // 서버에서 반환한 이미지 업데이트
    xhr.onreadystatechange = function() {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
          reload_image("preprocessingImage");
        }
    }
    // 슬라이더 값을 출력
    document.getElementById("sliderValue").innerHTML = this.value;
  });
}

function blob_action() {
  const blobvalue = document.getElementById("blobValue").value;
  // 서버로 슬라이더 값을 전송
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/action_blob", true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.send("value=" + blobvalue);
  // 서버에서 반환한 이미지 업데이트
  xhr.onreadystatechange = function() {
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      reload_image("preprocessingImage");
    }
  }
}

function blur_action() {
  const widthValue = document.getElementById("widthValue").value;
  const heightValue = document.getElementById("heightValue").value;
  const sigmaValue = document.getElementById("sigmaValue").value;
  const data = {"widthValue": widthValue, "heightValue": heightValue, "sigmaValue": sigmaValue}
  const jsonData = JSON.stringify(data);
  // 서버로 슬라이더 값을 전송
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/action_blur", true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(jsonData);
  // 서버에서 반환한 이미지 업데이트
  xhr.onreadystatechange = function() {
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      reload_image("preprocessingImage");
    }
  }
}