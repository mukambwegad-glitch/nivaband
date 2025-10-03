def build_prompt(genre, mood, instruments, bpm, duration, notes):
    return f"""
    Create a {mood} {genre} track with {instruments}.
    BPM: {bpm}, Duration: {duration}s.
    Extra notes: {notes}.
    Include cinematic melodies, layered textures, and professional-quality mix.
    """
