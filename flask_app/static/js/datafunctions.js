export const getSearchTerm = () => {
    const rawSearchTerm = document.getElementById('search').value.trim();
    const regex = /[ ]{2,}/gi;
    const searchTerm = rawSearchTerm.replaceAll(regex, " ");
    return searchTerm;
};

export const retrieveSearchResults = async (searchTerm) => {
    const apiSearchString = getApiSearchString(searchTerm);
    const apiSearchResults = await requestData(apiSearchString);
    let resultArray = [];
    if (apiSearchResults.hasOwnProperty("results")) {
        console.log("test2, query = true");
        resultArray = processApiResults(apiSearchResults.results); 
    }
    return resultArray;
};

const getApiSearchString = (searchTerm) => {
    const maxChars = getMaxChars();
    const rawSearchString = `https://api.jikan.moe/v3/search/anime?q=${searchTerm}&limit=30`;
    const searchString = encodeURI(rawSearchString);
    console.log(searchString)
    console.log('returns url link with search term')
    return searchString;
};

const getMaxChars = () => {
    const width = window.innerWidth || document.body.clientWidth;
    let maxChars;
    if (width < 414) maxChars = 65;
    if (width >= 414 && width < 1400) maxChars = 100;
    if (width >= 1400) maxChars = 130;
    return maxChars;
};

const requestData = async (searchString) => {
    try{
        const response = await fetch(searchString);
        const data = await response.json();
        console.log(data);
        return data;
    } catch (err) {
        console.error(err);
    }
};

const processApiResults = (results) => { 
    const resultArray = [];
    for (const item of results) {
    // Object.keys(results).forEach((key) => {
        // const id = key
        const id = item.mal_id;
        const title = item.title;
        const url = item.url;
        const img = item.hasOwnProperty('image_url')
        ? item.image_url
        : null;
        const data = {
            id: id,
            title: title,
            img: img,
            url: url,
        };
        resultArray.push(data);
    };
    return resultArray;
};