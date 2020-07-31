export function contrast(color: string): "black" | "white" {
    let rgb = color;

    if (rgb.startsWith("#")) {
        rgb = rgb.replace("#", "");
        const aRgbHex = rgb.match(/.{1,2}/g);
        if (!aRgbHex) return "white";
        const aRgb = [parseInt(aRgbHex[0], 16), parseInt(aRgbHex[1], 16), parseInt(aRgbHex[2], 16)];
        rgb = `rgb(${aRgb.join(",")})`;
    }

    console.log(rgb);

    // Strip everything except the integers eg. "rgb(" and ")" and " "
    rgb = rgb.split(/\(([^)]+)\)/)[1].replace(/ /g, "");

    console.log(rgb);

    // map RGB values to variables
    const r = parseInt(rgb.split(",")[0], 10);
    const g = parseInt(rgb.split(",")[1], 10);
    const b = parseInt(rgb.split(",")[2], 10);

    console.log(r);
    console.log(g);
    console.log(b);

    // calculate contrast of color (standard grayscale algorithmic formula)
    const num = (Math.round(r * 299) + Math.round(g * 587) + Math.round(b * 114)) / 1000;
    return num >= 128 ? "black" : "white";
}

export default contrast;
