(function() {
  window.addEventListener("load", init);
  function init() {
    qs("form").addEventListener("submit", function(e) {
      e.preventDefault();
      getFakeStoryWithDelay();
    });
  }

  function getFakeStoryWithDelay() {
    id("loading").classList.remove("hidden");
    setTimeout(() => {
      fetch("http://127.0.0.1:5000/get-gpt-story-fake")
        .then(checkStatus)
        .then(res => res.json())
        .then(processMultiSentenceResult)
        .catch(console.error)},
      2000);
  }
  function getStoryWithData() {
    id("loading").classList.remove("hidden");
    const data = new FormData(qs("form"));
    fetch("http://127.0.0.1:5000/get-gpt-story-with-prompt", {method: 'POST', body: data})
      .then(checkStatus)
      .then(res => res.json())
      .then(processMultiSentenceResult)
      .catch(console.error)
  }

  function processMultiSentenceResult(res) {
    id("loading").classList.add("hidden");
    pinyinList = res.pinyins;
    sentenceList = res.sentences;
    for (let i = 0; i < sentenceList.length; i++) {
      const formattedSentence = getSentence(pinyinList[i], sentenceList[i]);
      id("story").appendChild(formattedSentence);
    }
    const translation = gen("p");
    translation.textContent = res.translation;
    id("translation").appendChild(translation);
  }

  function getSentence(pinyin, sentence) {
    const sentenceContainer = gen("div");
    sentenceContainer.classList.add("sentence-container")
    for (let i = 0; i < pinyin.length; i++) {
      const formattedChar = getCharacter(pinyin[i], sentence[i]);
      sentenceContainer.appendChild(formattedChar);
    }
    return sentenceContainer;
  }

  function getCharacter(p, c) {
    const box = gen("div");
    box.classList.add("char-box");
    const pinyinBox = gen("p");
    if (p == "none") {
      p = " ";
    }
    pinyinBox.textContent = p;
    box.appendChild(pinyinBox);
    const charBox = gen("p");
    charBox.textContent = c;
    box.appendChild(charBox);
    return box;
  }

  /**
   * Checks if the Reponse object from the API call is valid.
   * @param {Object} res - The Response object from the API call
   * @returns {Object} the Response object from the API call if it is
   * valid. If it is not, return an error.
   */
  async function checkStatus(res) {
    if (!res.ok) {
      throw new Error(await res.text());
    }
    return res;
  }

  function id(name) {
    return document.getElementById(name);
  }

  function qs(selector) {
    return document.querySelector(selector);
  }

  function qsa(selector) {
    return document.querySelectorAll(selector);
  }

  function gen(tagName) {
    return document.createElement(tagName);
  }
})();