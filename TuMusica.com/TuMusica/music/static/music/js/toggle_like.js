function toggle_song_like(song_id) {
    $.ajax({
        url: "/like/song/" + song_id.toString(),
        method: "POST",
        success: function (result) {
            $("#like_button_" + song_id.toString()).html(result);
        }
    });
}