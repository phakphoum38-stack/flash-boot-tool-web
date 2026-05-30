async function uploadISO() {

    const file =
        document.getElementById("iso")
        .files[0]

    const form =
        new FormData()

    form.append(
        "file",
        file
    )

    const res =
        await fetch(
            "http://127.0.0.1:8000/upload",
            {
                method: "POST",
                body: form
            }
        )

    const data =
        await res.json()

    document
      .getElementById("log")
      .innerHTML =
      JSON.stringify(data)
}
