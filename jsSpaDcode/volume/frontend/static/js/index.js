import Dashboard from "./views/Dashboard.js"; 
import Posts from "./views/Posts.js";
import Settings from "./views/Settings.js";
import PostView from "./views/PostView.js";

const pathToRegex = path => new RegExp("^" + path.replace(/\//g, "\\/").replace(/:\w+/g, "(.+)") + "$"); //정규표현식


const getParams = match => {
    //the type of values is array
    const values = match.result.slice(1);
    const keys = Array.from(match.route.path.matchAll(/:(\w+)/g)).map(result => result[1]); //정규표현식

    return Object.fromEntries(keys.map((key, i) => {
        return [key, values[i]];
    }));
};

const navigateTo = url => {
    history.pushState(null, null, url);
    router();
};

const router = async () => {
    const routes = [
        { path: "/", view: Dashboard },
        { path: "/posts", view: Posts },
        { path: "/posts/:id", view: PostView},
        { path: "/settings", view: Settings },
    ];

    // Test each route for potential match
    // the type of potentialMatches is array    
    const potentialMatches = routes.map(route => {
        return {
            route: route,
            //same with isMatch: location.pathname === route.path
            //check if the path is matched
            result: location.pathname.match(pathToRegex(route.path)),

        };
    });

    //the type of match is object
    // let match;

    // for (let i = 0; i < potentialMatches.length; i++) {
    //     if (potentialMatches[i].result !== null) {
    //         match = potentialMatches[i];
    //         break;
    //     }
    // }
    let match = potentialMatches.find(potentialMatch => potentialMatch.result !== null);


    //undefined path
    if (!match) {
        match = {
            //dashboard
            route: routes[0],
            result: [location.pathname]
        };
    }

    const view = new match.route.view(getParams(match));

    document.querySelector("#app").innerHTML = await view.getHtml();

};

//for back and forward button in browser
window.addEventListener("popstate", router);

document.addEventListener("DOMContentLoaded", () => {
    document.body.addEventListener("click", e => {
    //만약에 클릭한게 data-link라면 새로고침하지 않고, url을 바꿔준다, router를 호출한다.
        if (e.target.matches("[data-link]")) {
            e.preventDefault();
            navigateTo(e.target.href);
        }
    });

    router();
});



// import Dashboard from "./views/Dashboard.js";
// import Posts from "./views/Posts.js";
// import PostView from "./views/PostView.js";
// import Settings from "./views/Settings.js";

// const pathToRegex = path => new RegExp("^" + path.replace(/\//g, "\\/").replace(/:\w+/g, "(.+)") + "$");

// const getParams = match => {
//     const values = match.result.slice(1);
//     const keys = Array.from(match.route.path.matchAll(/:(\w+)/g)).map(result => result[1]);

//     return Object.fromEntries(keys.map((key, i) => {
//         return [key, values[i]];
//     }));
// };

// const navigateTo = url => {
//     history.pushState(null, null, url);
//     router();
// };

// const router = async () => {
//     const routes = [
//         { path: "/", view: Dashboard },
//         { path: "/posts", view: Posts },
//         { path: "/posts/:id", view: PostView },
//         { path: "/settings", view: Settings }
//     ];

//     // Test each route for potential match
//     const potentialMatches = routes.map(route => {
//         return {
//             route: route,
//             result: location.pathname.match(pathToRegex(route.path))
//         };
//     });

//     let match = potentialMatches.find(potentialMatch => potentialMatch.result !== null);

//     if (!match) {
//         match = {
//             route: routes[0],
//             result: [location.pathname]
//         };
//     }

//     const view = new match.route.view(getParams(match));

//     document.querySelector("#app").innerHTML = await view.getHtml();
// };

// window.addEventListener("popstate", router);

// document.addEventListener("DOMContentLoaded", () => {
//     document.body.addEventListener("click", e => {
//         if (e.target.matches("[data-link]")) {
//             e.preventDefault();
//             navigateTo(e.target.href);
//         }
//     });

//     router();
// });