"""
Behavioral Pattern: Observer
-------------------------------
Defines a one-to-many dependency between objects so that when one
object (the Subject) changes state, all its dependents (Observers) are
notified automatically.

Example: a YouTubeChannel (Subject) that notifies all Subscribers
(Observers) whenever it uploads a new video.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, video_title: str) -> None:
        ...


class Subscriber(Observer):
    def __init__(self, name: str):
        self.name = name
        self.notifications = []

    def update(self, video_title: str) -> None:
        message = f"{self.name} notified: new video '{video_title}' uploaded!"
        self.notifications.append(message)
        print(message)


class YouTubeChannel:
    def __init__(self, name: str):
        self.name = name
        self._subscribers = []

    def subscribe(self, observer: Observer) -> None:
        self._subscribers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._subscribers.remove(observer)

    def upload_video(self, title: str) -> None:
        print(f"{self.name} uploaded: {title}")
        for subscriber in self._subscribers:
            subscriber.update(title)


if __name__ == "__main__":
    channel = YouTubeChannel("Deep Skilling Tech")
    aruna = Subscriber("Aruna")
    guest = Subscriber("Guest")

    channel.subscribe(aruna)
    channel.subscribe(guest)
    channel.upload_video("Design Patterns Explained")

    channel.unsubscribe(guest)
    channel.upload_video("DSA Crash Course")

    assert len(aruna.notifications) == 2
    assert len(guest.notifications) == 1
    print("Observer checks passed.")
