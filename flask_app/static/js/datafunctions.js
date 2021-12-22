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
    console.log(apiSearchResults); // <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Full data but not a query??
    console.log("test1")
    console.log(apiSearchResults.hasOwnProperty("query"))
    console.log('**************************************')
    if (apiSearchResults.hasOwnProperty("query")) {
        console.log("test2, query = true"); // <<<<<<< WHY isnt this printing???
        resultArray = processApiResults(apiSearchResults.query); // <<<<<<<< Passes through here
    }
    console.log("test3")
    console.log(resultArray); // <<<<<<<<<<<<<<<<<< Empty array
    return resultArray;
};

const getApiSearchString = (searchTerm) => {
    const maxChars = getMaxChars();
    const rawSearchString = `https://api.jikan.moe/v3/search/anime?q=${searchTerm}`;
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
        console.log(data); // <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Full data
        return data;
    } catch (err) {
        console.error(err);
    }
};

const processApiResults = (results) => {  // <<<<<<<<<<<<<<<<<< unsure if working
    const resultArray = [];
    Object.keys(results).forEach((key) => {
        // const id = key
        const id = results[key].mal_id;
        const title = results[key].title;
        const img = results[key].hasOwnProperty('image_url')
        ? results[key].image_url.source
        : null;
        const item = {
            id: id,
            title: title,
            img: img,
        };
        resultArray.push(item);
    });
    return resultArray;
};