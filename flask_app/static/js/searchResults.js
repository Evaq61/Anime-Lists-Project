export const deleteSearchResults = () => {
    const parentElement = document.getElementById("searchResults");
    let child = parentElement.lastElementChild;
    while (child) {
        parentElement.removeChild(child);
        child = parentElement.lastElementChild;
    }
};


export const buildSearchResults = (resultArray) => {
    resultArray.forEach(result => {
        const resultItem = createResultItem(result);
        const resultContents = document.createElement('div');
        resultContents.classList.add("resultContents");
        if (result.img) {
            const resultImage = createResultImage(result);
            resultContents.append(resultImage);
        }
        resultItem.append(resultContents);
        const searchResults = document.getElementById('searchResults');
        searchResults.append(resultItem);
    });
};

const createResultItem = (result) => {
    const resultItem = document.createElement('div');
    resultItem.classList.add('resultItem');
    const resultTitle = document.createElement('div');
    resultTitle.classList.add('resultTitle');
    const link = document.createElement('a');
    link.href = `/anime/info/${result.id}`;  // <<<< opens new link, can I make it not do that
    // link.href = result.url;  // <<<< opens new link to myanimelist.net = current placeholder
    // link.href = `https://api.jikan.moe/v3/anime/${result.id}`; // api request link using the anime title's mal_id in json text
    link.textContent = result.title;
    link.target = "_blank";
    resultTitle.append(link);
    resultItem.append(resultTitle);
    return resultItem;
};

const createResultImage = (result) => {
    const resultImage = document.createElement('div');
    resultImage.classList.add("resultImage");
    const img = document.createElement('img');
    img.src = result.img;
    img.alt = result.title;
    resultImage.append(img);
    return resultImage;
};

export const clearStatsLine = () => {
    document.getElementById('stats').textContent = "";
}

export const setStatsLine = (numberOfResults) => {
    const statLine = document.getElementById('stats');
    if (numberOfResults) {
        statLine.textContent = `Displaying ${numberOfResults} results`;
    } else {
        statLine.textContent = "Sorry, No Results";
    }
};

