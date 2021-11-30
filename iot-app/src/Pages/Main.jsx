import React from "react";

import Header from "../Components/Header";

export default function Main() {
  return (
    <div>
      <Header />
      <div
        className="tableauPlaceholder"
        id="viz1638284005185"
        style={{ position: "relative" }}
      >
        <noscript>
          <a href="https:&#47;&#47;www.tableau.com&#47;">
            <img
              alt="AAPL "
              src="https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;VG&#47;VGContest_AAPLTicker_YuriFal&#47;AAPL&#47;1_rss.png"
              style={{ border: "none" }}
            />
          </a>
        </noscript>
        <object className="tableauViz" style={{ display: "none" }}>
          <param name="host_url" value="https%3A%2F%2Fpublic.tableau.com%2F" />{" "}
          <param name="embed_code_version" value="3" />{" "}
          <param name="site_root" value="" />
          <param name="name" value="VGContest_AAPLTicker_YuriFal&#47;AAPL" />
          <param name="tabs" value="no" />
          <param name="toolbar" value="yes" />
          <param
            name="static_image"
            value="https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;VG&#47;VGContest_AAPLTicker_YuriFal&#47;AAPL&#47;1.png"
          />{" "}
          <param name="animate_transition" value="yes" />
          <param name="display_static_image" value="yes" />
          <param name="display_spinner" value="yes" />
          <param name="display_overlay" value="yes" />
          <param name="display_count" value="yes" />
        </object>
      </div>{" "}
      <script type="text/javascript">
        {" "}
        var divElement = document.getElementById('viz1638284005185'); var
        vizElement = divElement.getElementsByTagName('object')[0];
        vizElement.style.width='1200px';vizElement.style.height='627px'; var
        scriptElement = document.createElement('script'); scriptElement.src =
        'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);{" "}
      </script>
    </div>
  );
}
