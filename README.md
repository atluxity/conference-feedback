# Emoji Feedback Logging with Nginx

This project captures user feedback through emoji reactions on a webpage and logs it using Nginx. Users can click on emoji buttons (e.g., 😞, 😐, 😊) to provide feedback, which is then sent as a `GET` request to an Nginx server endpoint. Nginx logs the feedback data in a structured JSON format for further analysis.

## Features
- **Webpage with Emoji Feedback**: A simple HTML page where users can click on emoji buttons to provide feedback.
- **Feedback Logging**: Nginx logs each feedback submission, capturing details like the emoji and the time of submission.
- **Responsive Design**: The feedback page is styled to adapt to different screen sizes, ensuring usability across devices.
- **Minimal Server-Side Configuration**: Uses Nginx's logging capabilities to handle feedback without the need for additional backend services.

## Prerequisites
- **Nginx**: Ensure you have Nginx installed and configured on your server.
- **A Web Browser**: For accessing the feedback page.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/emoji-feedback-nginx.git
   cd emoji-feedback-nginx
   ```

2. **Configure Nginx**:
   Add the following to your Nginx configuration, under the relevant server clause (e.g., in `/etc/nginx/sites-available/default`):
   ```nginx
       location /log-feedback {
       access_log /var/log/nginx/emoji_feedback.log custom_json;
       return 204;  # Only after reading the body
    }
   ```

   Add the following to your Nginx configuration, under the relevant http clause (e.g., in `/etc/nginx/nginx.conf`):
   ```nginx
        log_format custom_json '{ "emoji": "$arg_emoji", "time": "$time_iso8601" }';
   ```

3. **Restart Nginx**:
   Apply the changes:
   ```bash
   sudo nginx -t #syntax check
   sudo systemctl restart nginx
   ```

## Usage

1. **Open the Webpage**:
   Navigate to `http://example.com` in your browser (replace `example.com` with your server's address).

2. **Provide Feedback**:
   Click on one of the emoji buttons (`😞`, `😐`, `😊`) to submit feedback. The selected emoji will be sent as a `GET` request with an associated timestamp.

3. **View Logged Feedback**:
   Feedback is logged in `/var/log/nginx/emoji_feedback.log` in JSON format. For example:
   ```
   { "emoji": "42", "time": "2024-10-10T22:43:44+02:00" }
   { "emoji": "45", "time": "2024-10-10T22:44:09+02:00" }
   { "emoji": "58", "time": "2024-10-10T22:44:10+02:00" }
   ```

## Mapping Emoji to Descriptions
The emoji feedback is sent using ASCII representations:
- `42`: 😊 (Happy)
- `45`: 😐 (Neutral)
- `58`: 😞 (Sad)

You can interpret these values in your logs for further analysis.

## Customization
- **Adjusting Emoji Mapping**: Update the `emoji_map` in `index.html` if you want to change which ASCII values are sent for each emoji.
- **Styling**: Modify `style.css` to change the appearance of the feedback page.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [Nginx](https://nginx.org/) for their powerful web server capabilities.
- [MDN Web Docs](https://developer.mozilla.org/) for documentation on web technologies.

```

### Explanation of the README Structure:
- **Overview**: Explains the purpose of the project.
- **Features**: Lists what the project does.
- **Prerequisites**: Specifies necessary software.
- **Installation**: Provides step-by-step instructions for setting up the project.
- **Usage**: Describes how to use the project, including accessing the web page and reading the logs.
- **Mapping Emoji to Descriptions**: Details how to interpret the data in the logs.
- **Customization**: Highlights how to adjust the project to fit specific needs.
- **Contributing**: Invites collaboration.
- **License**: Provides licensing information.

Feel free to copy this into a `README.md` file for your repository and adjust any sections as needed! Let me know if you need more help.
