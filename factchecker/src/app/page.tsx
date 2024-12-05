"use client";

import { Button, Input, Textarea } from "@nextui-org/react";
import axios from "axios";
import React, { useState } from "react";

export default function Home() {
  const [result, setResult] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [resultVisibilty, setResultVisibilty] = useState(false);
  const [data, setData] = useState({
    tweet: "",
    views: 0,
    bookmark_count: 0,
    favorite_count: 0,
    quote_count: 0,
    reply_count: 0,
    retweet_cout: 0,
  });
  return (
    <div className="flex justify-center pt-16 h-screen w-screen overflow-auto">
      <div className="flex flex-col gap-3 h-full items-center w-[60%] p-4">
        <div className="w-full flex justify-center">
          <Textarea
            label="Content"
            placeholder="Enter your description"
            className="max-w-full"
            onChange={(e) => {
              setData({ ...data, tweet: e.target.value });
            }}
          />
        </div>
        <div className="flex justify-between w-full">
          <Input
            type="number"
            className="w-[40%]"
            label="Views"
            placeholder="Enter Views"
            onChange={(e) => {
              setData({ ...data, views: Number(e.target.value) });
            }}
          />
          <Input
            type="number"
            className="w-[40%]"
            label="Bookmark Count"
            placeholder="Enter Bookmark Count"
            onChange={(e) => {
              setData({ ...data, bookmark_count: Number(e.target.value) });
            }}
          />
        </div>
        <div className="flex justify-between w-full">
          <Input
            type="number"
            className="w-[40%]"
            label="Favorite Count"
            placeholder="Enter Favorite Count"
            onChange={(e) => {
              setData({ ...data, favorite_count: Number(e.target.value) });
            }}
          />
          <Input
            type="number"
            className="w-[40%]"
            label="Quote Count"
            placeholder="Enter Bookmark Quote Count"
            onChange={(e) => {
              setData({ ...data, quote_count: Number(e.target.value) });
            }}
          />
        </div>
        <div className="flex justify-between w-full">
          <Input
            type="number"
            className="w-[40%]"
            label="Reply Count"
            placeholder="Enter Reply Count"
            onChange={(e) => {
              setData({ ...data, reply_count: Number(e.target.value) });
            }}
          />
          <Input
            type="number"
            className="w-[40%]"
            label="Retweet Count"
            placeholder="Enter Retweet Count"
            onChange={(e) => {
              setData({ ...data, retweet_cout: Number(e.target.value) });
            }}
          />
        </div>
        <div>
          <Button
            isLoading={isLoading }
            onClick={async () => {
              setIsLoading(true);
              const response = await axios.post(
                "http://localhost:8000/predict2",
                data
              );
              setResult(response.data?.prediction);
              setIsLoading(false);
            }}
            className="text-lg"
            variant="ghost"
            color="default"
          >
            Validate
          </Button>
        </div>
        <div
          className={`
            ${result === "" ? `hidden` : `block`} 
            ${
              result === "Fact"
                ? `bg-green-950  border-green-950`
                : `bg-red-600  border-red-600`
            } 
          px-4 py-1 font-extrabold text-xl text-white hover:bg-opacity-100 cursor-pointer rounded-lg border-3 bg-opacity-30 `}
        >
          It's a {result}
        </div>
      </div>
    </div>
  );
}
