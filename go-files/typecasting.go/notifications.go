package main

import (
	"encoding/json"
	"fmt"
)

type CreateRequest struct {
	NotificationName string `json:"notification_name"`
	Language         string `json:"language"`
	Template         string `json:"template"`
}

/*func main2() {
	fmt.Println("Hello, playground")

	req := `{"notification_name": "watchable","language": "en", "template": "{\"new_video\": {\"movie\": {\"title\": \"%s\",\"description\": \"Available now!\"},\"episode\": {\"title\": \"%s\",\"description\": \"Episode %s: Available now!\"}}}"
}`


    r, ok := req.(CreateRequest)
	if !ok {
			fmt.Printf("err=%v\n", "bad syntax")
		}
}
*/

// Video Info
type VideoInfo struct {
	Video VideoSection `json:"video"`
}

type VideoSection struct {
	ID        string            `json:"id"`
	Titles    map[string]string `json:"titles"`
	Container Container         `json:"container"`
}

type Container struct {
	ID     string            `json:"id"`
	Titles map[string]string `json:"titles"`
	URL    string            `json:"url"`
}

func fakemain() {

	payload := `{"video":{"id":"1167658v","content_owners":[{"id":"358co"}],"created_at":"2020-06-04T10:19:38Z","updated_at":"2020-06-17T15:14:19Z","type":"episode","duration":2700,"number":16,"root_id":"1150712vr","origin":{"language":"zh"},"titles":{},"titles_phonetic":{},"titles_aka":{},"kaltura_id":null,"descriptions":{},"subtitle_completions":{},"container":{"id":"36951c","type":"series","subtype":"normal","titles":{"en":"You Are My Destiny","zh":"你是我的命中注定","zt":"你是我的命中註定","de":"You Are My Destiny","ja":"You Are My Destiny","it":"Sei Il Mio Destino","ko":"니시아적명중주종(You Are My Destiny)","pt":"You Are My Destiny","fr":"Tu es ma destinée","es":"Tú eres mi destino"},"team_name":"Fated to Love","genres":["18g","9g"],"origin":{"country":"cn","language":"zh"},"managers":[{"id":"10566233u","username":"machadosteff","images":{"avatar":{"url":null}},"url":{"web":"https://www.viki.com/users/machadosteff","api":"https://api.viki.io/v4/users/10566233u.json"}}],"images":{"atv_cover":{"url":"https://6.vikiplatform.com/image/c09d84fc63c8406bb280db92ce7cd4d0.jpg?x=b&a=0x0","source":"viki"},"poster":{"url":"https://6.vikiplatform.com/image/f50be54d9e16469fbeaaf2b2cb359b68.jpg?x=b&a=0x0","source":"viki"}},"url":{"web":"https://www.viki.com/tv/36951c-you-are-my-destiny","api":"https://api.viki.io/v4/series/36951c.json"},"review_stats":{"average_rating":9.35,"count":1286},"planned_episodes":36},"hardsubs":[],"hardsub_languages":[],"source":"viki","images":{"poster":{"url":"https://6.vikiplatform.com/image/62ebd51949b4473a970f478f9130e48d.jpg?x=b&a=0x0","source":"viki"}},"likes":{"count":0},"flags":{"licensed":true,"hosted":true,"on_air":true,"embeddable":true,"state":"normal","adult":false,"hd":true,"has_stream":true},"url":{"api":"https://api.viki.io/v4/videos/1167658v.json","fb":"https://www.viki.com/videos/1167658v-you-are-my-destiny-episode-16","web":"https://www.viki.com/videos/1167658v-you-are-my-destiny-episode-16"},"embed":{"iframe":{"url":"https://www.viki.com/player/1167658v"}},"rating":"PG-13","parts":[{"id":"1167658v","part":1,"url":"https://api.viki.io/v4/videos/1167658v.json"}],"viki_air_time":1592409600,"credits_marker":2611,"part_index":0,"author":"Tencent","author_url":"https://www.viki.com/networks/358co-tencent","blocked":false,"blocking":{"geo":false,"paywall":false,"upcoming":false}},"country":"jp"}`

	info := VideoInfo{}

	bytesPayload, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("err=%v\n", err)
	}
	err = json.Unmarshal(bytesPayload, &info)
	if err != nil {
		fmt.Printf("2-err=%v\n", err)
	}

	fmt.Printf("info=%v\n", info.Video.Container.ID)
}

type Obj struct {
	Title       string `json:"title"`
	Description string `json:"description"`
}
type NewVideo struct {
	Movie   Obj `json:"movie"`
	Episode Obj `json:"episode"`
}
type TemplateObj struct {
	NewVideo NewVideo `json:"new_video"`
}

func main() {
	in :="{\"new_video\":{\"movie\":{\"title\":\"%s\",\"description\":\"Available now!\"},\"episode\":{\"title\":\"%s\",\"description\":\"Episode %s: Available now!\"}}}"
	rawIn := json.RawMessage(in)
    bytes, err := rawIn.MarshalJSON()
    if err != nil {
        panic(err)
	}
	var T TemplateObj
	err = json.Unmarshal(bytes, &T)
    if err != nil {
        panic(err)
    }

    fmt.Printf("%+v", T)
}