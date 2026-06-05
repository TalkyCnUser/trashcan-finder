# 🗑️ Nearby Trashcan Finder

A simple web app that shows nearby trashcans and recycling bins on an interactive map. Built for a programming homework assignment.

## Live Demo

Open `index.html` in any modern browser.

## Features

- 📍 **Auto-detects your location** using browser GPS
- 🗑️ **Finds real trashcans** via the free OpenStreetMap (Overpass) API
- 🗺️ **Interactive map** with clickable markers
- 📏 **Adjustable search radius** (100m – 5km)
- 🔍 **Address search** fallback if GPS is unavailable
- 🧭 **Google Maps directions** for every trashcan

## Tech Stack

- HTML5 + vanilla JavaScript
- [Leaflet.js](https://leafletjs.com/) (map)
- [Tailwind CSS](https://tailwindcss.com/) (styling)
- [Overpass API](https://overpass-api.de/) (trashcan data)
- [Nominatim](https://nominatim.org/) (geocoding)

## How to Run

Simply open `index.html` in your browser, or serve it locally:

```bash
npx serve .
```

Then visit `http://localhost:3000`.

## Screenshot

*(Add a screenshot here if required by your assignment)*

## Homework Info

- **Course:** *(fill in)*
- **Student:** *(fill in)*
- **Date:** *(fill in)*
