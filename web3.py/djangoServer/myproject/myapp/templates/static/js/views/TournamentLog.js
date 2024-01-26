import AbstractView from "./AbstractView.js";

export default class extends AbstractView {
    constructor(params) {
        super(params);
        this.setTitle("Tournament Log");
    }

    async getHtml() {

        await fetch('/tournament/log')
            .then(response => response.json())
            .then(data => console.log(data));

        return `
            <h1>Tournament</h1>
            <p>Manage your privacy and configuration.</p>
        `;

    }
}