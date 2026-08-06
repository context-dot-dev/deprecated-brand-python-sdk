# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import (
    brand_fonts_params,
    brand_ai_query_params,
    brand_prefetch_params,
    brand_retrieve_params,
    brand_ai_product_params,
    brand_screenshot_params,
    brand_styleguide_params,
    brand_ai_products_params,
    brand_web_scrape_md_params,
    brand_retrieve_naics_params,
    brand_web_scrape_html_params,
    brand_retrieve_by_isin_params,
    brand_retrieve_by_name_params,
    brand_prefetch_by_email_params,
    brand_retrieve_by_email_params,
    brand_web_scrape_images_params,
    brand_retrieve_by_ticker_params,
    brand_web_scrape_sitemap_params,
    brand_retrieve_simplified_params,
    brand_identify_from_transaction_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.brand_fonts_response import BrandFontsResponse
from ..types.brand_ai_query_response import BrandAIQueryResponse
from ..types.brand_prefetch_response import BrandPrefetchResponse
from ..types.brand_retrieve_response import BrandRetrieveResponse
from ..types.brand_ai_product_response import BrandAIProductResponse
from ..types.brand_screenshot_response import BrandScreenshotResponse
from ..types.brand_styleguide_response import BrandStyleguideResponse
from ..types.brand_ai_products_response import BrandAIProductsResponse
from ..types.brand_web_scrape_md_response import BrandWebScrapeMdResponse
from ..types.brand_retrieve_naics_response import BrandRetrieveNaicsResponse
from ..types.brand_web_scrape_html_response import BrandWebScrapeHTMLResponse
from ..types.brand_retrieve_by_isin_response import BrandRetrieveByIsinResponse
from ..types.brand_retrieve_by_name_response import BrandRetrieveByNameResponse
from ..types.brand_prefetch_by_email_response import BrandPrefetchByEmailResponse
from ..types.brand_retrieve_by_email_response import BrandRetrieveByEmailResponse
from ..types.brand_web_scrape_images_response import BrandWebScrapeImagesResponse
from ..types.brand_retrieve_by_ticker_response import BrandRetrieveByTickerResponse
from ..types.brand_web_scrape_sitemap_response import BrandWebScrapeSitemapResponse
from ..types.brand_retrieve_simplified_response import BrandRetrieveSimplifiedResponse
from ..types.brand_identify_from_transaction_response import BrandIdentifyFromTransactionResponse

__all__ = ["BrandResource", "AsyncBrandResource"]


class BrandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/deprecated-brand-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/deprecated-brand-python-sdk#with_streaming_response
        """
        return BrandResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        domain: str | Omit = omit,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        ticker: str | Omit = omit,
        ticker_exchange: Literal[
            "AMEX",
            "AMS",
            "AQS",
            "ASX",
            "ATH",
            "BER",
            "BME",
            "BRU",
            "BSE",
            "BUD",
            "BUE",
            "BVC",
            "CBOE",
            "CNQ",
            "CPH",
            "DFM",
            "DOH",
            "DUB",
            "DUS",
            "DXE",
            "EGX",
            "FSX",
            "HAM",
            "HEL",
            "HKSE",
            "HOSE",
            "ICE",
            "IOB",
            "IST",
            "JKT",
            "JNB",
            "JPX",
            "KLS",
            "KOE",
            "KSC",
            "KUW",
            "LIS",
            "LSE",
            "MCX",
            "MEX",
            "MIL",
            "MUN",
            "NASDAQ",
            "NEO",
            "NSE",
            "NYSE",
            "NZE",
            "OSL",
            "OTC",
            "PAR",
            "PNK",
            "PRA",
            "RIS",
            "SAO",
            "SAU",
            "SES",
            "SET",
            "SGO",
            "SHH",
            "SHZ",
            "SIX",
            "STO",
            "STU",
            "TAI",
            "TAL",
            "TLV",
            "TSX",
            "TSXV",
            "TWO",
            "VIE",
            "WSE",
            "XETRA",
        ]
        | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """
        Retrieve logos, backdrops, colors, industry, description, and more from any
        domain

        Args:
          domain: Domain name to retrieve brand data for (e.g., 'example.com', 'google.com').
              Cannot be used with name or ticker parameters.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data. Works with all three lookup methods.

          name: Company name to retrieve brand data for (e.g., 'Apple Inc'). Cannot be used with
              domain or ticker parameters.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          ticker: Stock ticker symbol to retrieve brand data for (e.g., 'AAPL'). Cannot be used
              with domain or name parameters.

          ticker_exchange: Stock exchange code.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "name": name,
                        "tags": tags,
                        "ticker": ticker,
                        "ticker_exchange": ticker_exchange,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_params.BrandRetrieveParams,
                ),
            ),
            cast_to=BrandRetrieveResponse,
        )

    def ai_product(
        self,
        *,
        url: str,
        max_age_ms: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductResponse:
        """
        Given a single URL, determines if it is a product page and extracts the product
        information.

        Args:
          url: The product page URL to extract product data from.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/ai/product",
            body=maybe_transform(
                {
                    "url": url,
                    "max_age_ms": max_age_ms,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                brand_ai_product_params.BrandAIProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIProductResponse,
        )

    @overload
    def ai_products(
        self,
        *,
        domain: str,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        """Extract product information from a brand's website.

        We will analyze the website
        and return a list of products with details such as name, description, image,
        pricing, features, and more.

        Args:
          domain: The domain name to analyze.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_products: Maximum number of products to extract.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def ai_products(
        self,
        *,
        direct_url: str,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        """Extract product information from a brand's website.

        We will analyze the website
        and return a list of products with details such as name, description, image,
        pricing, features, and more.

        Args:
          direct_url: A specific URL to use directly as the starting point for extraction without
              domain resolution.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_products: Maximum number of products to extract.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["domain"], ["direct_url"])
    def ai_products(
        self,
        *,
        domain: str | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        direct_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        return self._post(
            "/brand/ai/products",
            body=maybe_transform(
                {
                    "domain": domain,
                    "max_age_ms": max_age_ms,
                    "max_products": max_products,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                    "direct_url": direct_url,
                },
                brand_ai_products_params.BrandAIProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIProductsResponse,
        )

    def ai_query(
        self,
        *,
        data_to_extract: Iterable[brand_ai_query_params.DataToExtract],
        domain: str,
        specific_pages: brand_ai_query_params.SpecificPages | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIQueryResponse:
        """Use AI to extract specific data points from a brand's website.

        The AI will crawl
        the website and extract the requested information based on the provided data
        points.

        Args:
          data_to_extract: Array of data points to extract from the website

          domain: The domain name to analyze

          specific_pages: Optional object specifying which pages to analyze

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/ai/query",
            body=maybe_transform(
                {
                    "data_to_extract": data_to_extract,
                    "domain": domain,
                    "specific_pages": specific_pages,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                brand_ai_query_params.BrandAIQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIQueryResponse,
        )

    def fonts(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandFontsResponse:
        """
        Scrape font information from a website including font families, usage
        statistics, fallbacks, and element/word counts.

        Args:
          direct_url: A specific URL to fetch fonts from directly, bypassing domain resolution (e.g.,
              'https://example.com/design-system'). When provided, fonts are extracted from
              this exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to extract fonts from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/fonts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_fonts_params.BrandFontsParams,
                ),
            ),
            cast_to=BrandFontsResponse,
        )

    def identify_from_transaction(
        self,
        *,
        transaction_info: str,
        city: str | Omit = omit,
        country_gl: Literal[
            "af",
            "al",
            "dz",
            "as",
            "ad",
            "ao",
            "ai",
            "aq",
            "ag",
            "ar",
            "am",
            "aw",
            "au",
            "at",
            "az",
            "bs",
            "bh",
            "bd",
            "bb",
            "by",
            "be",
            "bz",
            "bj",
            "bm",
            "bt",
            "bo",
            "ba",
            "bw",
            "bv",
            "br",
            "io",
            "bn",
            "bg",
            "bf",
            "bi",
            "kh",
            "cm",
            "ca",
            "cv",
            "ky",
            "cf",
            "td",
            "cl",
            "cn",
            "cx",
            "cc",
            "co",
            "km",
            "cg",
            "cd",
            "ck",
            "cr",
            "ci",
            "hr",
            "cu",
            "cy",
            "cz",
            "dk",
            "dj",
            "dm",
            "do",
            "ec",
            "eg",
            "sv",
            "gq",
            "er",
            "ee",
            "et",
            "fk",
            "fo",
            "fj",
            "fi",
            "fr",
            "gf",
            "pf",
            "tf",
            "ga",
            "gm",
            "ge",
            "de",
            "gh",
            "gi",
            "gr",
            "gl",
            "gd",
            "gp",
            "gu",
            "gt",
            "gn",
            "gw",
            "gy",
            "ht",
            "hm",
            "va",
            "hn",
            "hk",
            "hu",
            "is",
            "in",
            "id",
            "ir",
            "iq",
            "ie",
            "il",
            "it",
            "jm",
            "jp",
            "jo",
            "kz",
            "ke",
            "ki",
            "kp",
            "kr",
            "kw",
            "kg",
            "la",
            "lv",
            "lb",
            "ls",
            "lr",
            "ly",
            "li",
            "lt",
            "lu",
            "mo",
            "mk",
            "mg",
            "mw",
            "my",
            "mv",
            "ml",
            "mt",
            "mh",
            "mq",
            "mr",
            "mu",
            "yt",
            "mx",
            "fm",
            "md",
            "mc",
            "mn",
            "ms",
            "ma",
            "mz",
            "mm",
            "na",
            "nr",
            "np",
            "nl",
            "an",
            "nc",
            "nz",
            "ni",
            "ne",
            "ng",
            "nu",
            "nf",
            "mp",
            "no",
            "om",
            "pk",
            "pw",
            "ps",
            "pa",
            "pg",
            "py",
            "pe",
            "ph",
            "pn",
            "pl",
            "pt",
            "pr",
            "qa",
            "re",
            "ro",
            "ru",
            "rw",
            "sh",
            "kn",
            "lc",
            "pm",
            "vc",
            "ws",
            "sm",
            "st",
            "sa",
            "sn",
            "rs",
            "sc",
            "sl",
            "sg",
            "sk",
            "si",
            "sb",
            "so",
            "za",
            "gs",
            "es",
            "lk",
            "sd",
            "sr",
            "sj",
            "sz",
            "se",
            "ch",
            "sy",
            "tw",
            "tj",
            "tz",
            "th",
            "tl",
            "tg",
            "tk",
            "to",
            "tt",
            "tn",
            "tr",
            "tm",
            "tc",
            "tv",
            "ug",
            "ua",
            "ae",
            "gb",
            "us",
            "um",
            "uy",
            "uz",
            "vu",
            "ve",
            "vn",
            "vg",
            "vi",
            "wf",
            "eh",
            "ye",
            "zm",
            "zw",
        ]
        | Omit = omit,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        high_confidence_only: Union[bool, Literal["true", "false"]] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        mcc: Union[str, float] | Omit = omit,
        phone: Union[str, float] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandIdentifyFromTransactionResponse:
        """
        Endpoint specially designed for platforms that want to identify transaction data
        by the transaction title.

        Args:
          transaction_info: Transaction information to identify the brand

          city: Optional city name to prioritize when searching for the brand.

          country_gl: Two-letter ISO 3166-1 alpha-2 country code (GL parameter) used to localize
              search.

          force_language: Language to force for the retrieved brand data.

          high_confidence_only: When set to true, the API will perform an additional verification steps to
              ensure the identified brand matches the transaction with high confidence.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          mcc: Optional Merchant Category Code (MCC) to help identify the business
              category/industry.

          phone: Optional phone number from the transaction to help verify brand match.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/transaction_identifier",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "transaction_info": transaction_info,
                        "city": city,
                        "country_gl": country_gl,
                        "force_language": force_language,
                        "high_confidence_only": high_confidence_only,
                        "max_speed": max_speed,
                        "mcc": mcc,
                        "phone": phone,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_identify_from_transaction_params.BrandIdentifyFromTransactionParams,
                ),
            ),
            cast_to=BrandIdentifyFromTransactionResponse,
        )

    def prefetch(
        self,
        *,
        domain: str,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandPrefetchResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency.

        Args:
          domain: Domain name to prefetch brand data for

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/prefetch",
            body=maybe_transform(
                {
                    "domain": domain,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                brand_prefetch_params.BrandPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchResponse,
        )

    def prefetch_by_email(
        self,
        *,
        email: str,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandPrefetchByEmailResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency. This endpoint accepts an email address, extracts the domain from it,
        validates that it's not a disposable or free email provider, and queues the
        domain for prefetching.

        Args:
          email: Email address to prefetch brand data for. The domain will be extracted from the
              email. Free email providers (gmail.com, yahoo.com, etc.) and disposable email
              addresses are not allowed.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/prefetch-by-email",
            body=maybe_transform(
                {
                    "email": email,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                brand_prefetch_by_email_params.BrandPrefetchByEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchByEmailResponse,
        )

    def retrieve_by_email(
        self,
        *,
        email: str,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByEmailResponse:
        """
        Retrieve brand information using an email address while detecting disposable and
        free email addresses. Disposable and free email addresses (like gmail.com,
        yahoo.com) will throw a 422 error.

        Args:
          email: Email address to retrieve brand data for (e.g., 'contact@example.com'). The
              domain will be extracted from the email. Free email providers (gmail.com,
              yahoo.com, etc.) and disposable email addresses are not allowed.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-by-email",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_email_params.BrandRetrieveByEmailParams,
                ),
            ),
            cast_to=BrandRetrieveByEmailResponse,
        )

    def retrieve_by_isin(
        self,
        *,
        isin: str,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByIsinResponse:
        """
        Retrieve brand information using an ISIN (International Securities
        Identification Number).

        Args:
          isin: ISIN (International Securities Identification Number) to retrieve brand data for
              (e.g., 'AU000000IMD5', 'US0378331005'). Must be exactly 12 characters: 2 letters
              followed by 9 alphanumeric characters and ending with a digit.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-by-isin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "isin": isin,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_isin_params.BrandRetrieveByIsinParams,
                ),
            ),
            cast_to=BrandRetrieveByIsinResponse,
        )

    def retrieve_by_name(
        self,
        *,
        name: str,
        country_gl: Literal[
            "af",
            "al",
            "dz",
            "as",
            "ad",
            "ao",
            "ai",
            "aq",
            "ag",
            "ar",
            "am",
            "aw",
            "au",
            "at",
            "az",
            "bs",
            "bh",
            "bd",
            "bb",
            "by",
            "be",
            "bz",
            "bj",
            "bm",
            "bt",
            "bo",
            "ba",
            "bw",
            "bv",
            "br",
            "io",
            "bn",
            "bg",
            "bf",
            "bi",
            "kh",
            "cm",
            "ca",
            "cv",
            "ky",
            "cf",
            "td",
            "cl",
            "cn",
            "cx",
            "cc",
            "co",
            "km",
            "cg",
            "cd",
            "ck",
            "cr",
            "ci",
            "hr",
            "cu",
            "cy",
            "cz",
            "dk",
            "dj",
            "dm",
            "do",
            "ec",
            "eg",
            "sv",
            "gq",
            "er",
            "ee",
            "et",
            "fk",
            "fo",
            "fj",
            "fi",
            "fr",
            "gf",
            "pf",
            "tf",
            "ga",
            "gm",
            "ge",
            "de",
            "gh",
            "gi",
            "gr",
            "gl",
            "gd",
            "gp",
            "gu",
            "gt",
            "gn",
            "gw",
            "gy",
            "ht",
            "hm",
            "va",
            "hn",
            "hk",
            "hu",
            "is",
            "in",
            "id",
            "ir",
            "iq",
            "ie",
            "il",
            "it",
            "jm",
            "jp",
            "jo",
            "kz",
            "ke",
            "ki",
            "kp",
            "kr",
            "kw",
            "kg",
            "la",
            "lv",
            "lb",
            "ls",
            "lr",
            "ly",
            "li",
            "lt",
            "lu",
            "mo",
            "mk",
            "mg",
            "mw",
            "my",
            "mv",
            "ml",
            "mt",
            "mh",
            "mq",
            "mr",
            "mu",
            "yt",
            "mx",
            "fm",
            "md",
            "mc",
            "mn",
            "ms",
            "ma",
            "mz",
            "mm",
            "na",
            "nr",
            "np",
            "nl",
            "an",
            "nc",
            "nz",
            "ni",
            "ne",
            "ng",
            "nu",
            "nf",
            "mp",
            "no",
            "om",
            "pk",
            "pw",
            "ps",
            "pa",
            "pg",
            "py",
            "pe",
            "ph",
            "pn",
            "pl",
            "pt",
            "pr",
            "qa",
            "re",
            "ro",
            "ru",
            "rw",
            "sh",
            "kn",
            "lc",
            "pm",
            "vc",
            "ws",
            "sm",
            "st",
            "sa",
            "sn",
            "rs",
            "sc",
            "sl",
            "sg",
            "sk",
            "si",
            "sb",
            "so",
            "za",
            "gs",
            "es",
            "lk",
            "sd",
            "sr",
            "sj",
            "sz",
            "se",
            "ch",
            "sy",
            "tw",
            "tj",
            "tz",
            "th",
            "tl",
            "tg",
            "tk",
            "to",
            "tt",
            "tn",
            "tr",
            "tm",
            "tc",
            "tv",
            "ug",
            "ua",
            "ae",
            "gb",
            "us",
            "um",
            "uy",
            "uz",
            "vu",
            "ve",
            "vn",
            "vg",
            "vi",
            "wf",
            "eh",
            "ye",
            "zm",
            "zw",
        ]
        | Omit = omit,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByNameResponse:
        """
        Retrieve brand information using a company name.

        Args:
          name: Company name to retrieve brand data for (e.g., 'Apple Inc', 'Microsoft
              Corporation'). Must be 3-30 characters.

          country_gl: Two-letter ISO 3166-1 alpha-2 country code (GL parameter) used to localize
              search.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-by-name",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "country_gl": country_gl,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_name_params.BrandRetrieveByNameParams,
                ),
            ),
            cast_to=BrandRetrieveByNameResponse,
        )

    def retrieve_by_ticker(
        self,
        *,
        ticker: str,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        ticker_exchange: Literal[
            "AMEX",
            "AMS",
            "AQS",
            "ASX",
            "ATH",
            "BER",
            "BME",
            "BRU",
            "BSE",
            "BUD",
            "BUE",
            "BVC",
            "CBOE",
            "CNQ",
            "CPH",
            "DFM",
            "DOH",
            "DUB",
            "DUS",
            "DXE",
            "EGX",
            "FSX",
            "HAM",
            "HEL",
            "HKSE",
            "HOSE",
            "ICE",
            "IOB",
            "IST",
            "JKT",
            "JNB",
            "JPX",
            "KLS",
            "KOE",
            "KSC",
            "KUW",
            "LIS",
            "LSE",
            "MCX",
            "MEX",
            "MIL",
            "MUN",
            "NASDAQ",
            "NEO",
            "NSE",
            "NYSE",
            "NZE",
            "OSL",
            "OTC",
            "PAR",
            "PNK",
            "PRA",
            "RIS",
            "SAO",
            "SAU",
            "SES",
            "SET",
            "SGO",
            "SHH",
            "SHZ",
            "SIX",
            "STO",
            "STU",
            "TAI",
            "TAL",
            "TLV",
            "TSX",
            "TSXV",
            "TWO",
            "VIE",
            "WSE",
            "XETRA",
        ]
        | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByTickerResponse:
        """
        Retrieve brand information using a stock ticker symbol.

        Args:
          ticker: Stock ticker symbol to retrieve brand data for (e.g., 'AAPL', 'GOOGL', 'BRK.A').
              Must be 1-15 characters, letters/numbers/dots only.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          ticker_exchange: Stock exchange code.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-by-ticker",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ticker": ticker,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "tags": tags,
                        "ticker_exchange": ticker_exchange,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_ticker_params.BrandRetrieveByTickerParams,
                ),
            ),
            cast_to=BrandRetrieveByTickerResponse,
        )

    def retrieve_naics(
        self,
        *,
        input: str,
        max_results: int | Omit = omit,
        min_results: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveNaicsResponse:
        """
        Classify any brand into 2022 NAICS industry codes from its domain or name.

        Args:
          input: Brand domain or title to retrieve NAICS code for. If a valid domain is provided,
              it will be used for classification, otherwise, we will search for the brand
              using the provided title.

          max_results: Maximum number of NAICS codes to return. Must be between 1 and 10. Defaults
              to 5.

          min_results: Minimum number of NAICS codes to return. Must be at least 1. Defaults to 1.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/naics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "input": input,
                        "max_results": max_results,
                        "min_results": min_results,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_naics_params.BrandRetrieveNaicsParams,
                ),
            ),
            cast_to=BrandRetrieveNaicsResponse,
        )

    def retrieve_simplified(
        self,
        *,
        domain: str,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        theme: Literal["light", "dark"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveSimplifiedResponse:
        """
        Returns a simplified version of brand data containing only essential
        information: domain, title, colors, logos, and backdrops. Optimized for faster
        responses and reduced data transfer.

        Args:
          domain: Domain name to retrieve simplified brand data for

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          theme: Optional theme preference used when selecting brand assets.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-simplified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "theme": theme,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_simplified_params.BrandRetrieveSimplifiedParams,
                ),
            ),
            cast_to=BrandRetrieveSimplifiedResponse,
        )

    def screenshot(
        self,
        *,
        color_scheme: Literal["light", "dark"] | Omit = omit,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        handle_cookie_popup: Union[bool, Literal["true", "false"]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        scroll_offset: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        viewport: brand_screenshot_params.Viewport | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandScreenshotResponse:
        """
        Capture a screenshot of a website.

        Args:
          color_scheme: Optional parameter to choose the site's visual theme in the screenshot. Use
              'light' or 'dark' when the site offers both appearances.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          handle_cookie_popup: Optional parameter to control cookie/consent popup handling. If 'true', we
              dismiss cookie banner before capture. If 'false' or not provided, captures the
              page without that step.

          max_age_ms: Return a cached screenshot if a prior screenshot for the same parameters exists
              and is younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always capture fresh.

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          scroll_offset: Optional vertical scroll offset in pixels for capturing a long page in
              viewport-sized chunks. When provided, the full page is captured once and the
              returned image is the viewport-sized slice that begins at this Y offset (e.g.
              request scrollOffset=0, then 1080, then 2160 to walk a 1920x1080 landing page
              top to bottom). The final slice may be shorter than the viewport height. Takes
              precedence over fullScreenshot. Max: 100000.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          viewport: Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080.

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before taking
              the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
              omitted.

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "color_scheme": color_scheme,
                        "country": country,
                        "direct_url": direct_url,
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "handle_cookie_popup": handle_cookie_popup,
                        "max_age_ms": max_age_ms,
                        "page": page,
                        "scroll_offset": scroll_offset,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "viewport": viewport,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
                    },
                    brand_screenshot_params.BrandScreenshotParams,
                ),
            ),
            cast_to=BrandScreenshotResponse,
        )

    def styleguide(
        self,
        *,
        color_scheme: Literal["light", "dark"] | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandStyleguideResponse:
        """
        Extract a comprehensive design system from a website including colors,
        typography, spacing, shadows, and UI components.

        Args:
          color_scheme: Optional browser color scheme to emulate for websites that respond to
              prefers-color-scheme. This value is part of the styleguide cache key.

          direct_url: A specific URL to fetch the styleguide from directly, bypassing domain
              resolution (e.g., 'https://example.com/design-system'). When provided, the
              styleguide is extracted from this exact URL. You must provide either 'domain' or
              'directUrl', but not both.

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/styleguide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "color_scheme": color_scheme,
                        "direct_url": direct_url,
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_styleguide_params.BrandStyleguideParams,
                ),
            ),
            cast_to=BrandStyleguideResponse,
        )

    def web_scrape_html(
        self,
        *,
        url: str,
        actions: Optional[Iterable[brand_web_scrape_html_params.Action]] | Omit = omit,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        exclude_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        include_frames: Union[bool, Literal["true", "false"]] | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        pdf: brand_web_scrape_html_params.Pdf | Omit = omit,
        settle_animations: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: Union[bool, Literal["true", "false"]] | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeHTMLResponse:
        """Scrapes the given URL and returns the raw HTML content of the page.

        The base
        request costs 1 credit; requests with browser actions cost 2 credits.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove from the result. Applied after includeSelectors.
              Exclusion takes precedence: an element matching both is removed. Examples:
              "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          include_frames: When true, iframes are rendered inline into the returned HTML.

          include_selectors: CSS selectors. When provided, only matching subtrees (and their descendants) are
              kept and everything else is dropped. When omitted, the entire document is kept.
              Examples: "article.main", "#content", "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              extracting HTML. Defaults to false. This adds a bit of latency in exchange for
              more stable output on animated pages.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: When true, return only the page's main content in the HTML response, excluding
              headers, footers, sidebars, and navigation when detectable.

          wait_for_ms:
              Optional browser wait time in milliseconds after initial page load. Min: 0. Max:
              30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "actions": actions,
                        "country": country,
                        "exclude_selectors": exclude_selectors,
                        "headers": headers,
                        "include_frames": include_frames,
                        "include_selectors": include_selectors,
                        "max_age_ms": max_age_ms,
                        "pdf": pdf,
                        "settle_animations": settle_animations,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
                    },
                    brand_web_scrape_html_params.BrandWebScrapeHTMLParams,
                ),
            ),
            cast_to=BrandWebScrapeHTMLResponse,
        )

    def web_scrape_images(
        self,
        *,
        url: str,
        actions: Optional[Iterable[brand_web_scrape_images_params.Action]] | Omit = omit,
        dedupe: Union[bool, Literal["true", "false"]] | Omit = omit,
        enrichment: Optional[brand_web_scrape_images_params.Enrichment] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeImagesResponse:
        """
        Extract image assets from a web page, including standard URLs, inline SVGs, data
        URIs, responsive image sources, metadata, CSS backgrounds, video posters, and
        embeds. The base request costs 1 credit, or 2 credits with browser actions. When
        enrichment is enabled, the entire call costs 5 credits, including requests that
        also use actions.

        Args:
          url: Page URL to inspect. Must include http:// or https://.

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          dedupe: When true, visually duplicate images are removed: every image is loaded and
              perceptually hashed, and only the highest-resolution copy of each duplicate
              group is kept. Images that cannot be downloaded or hashed are kept. Default:
              false.

          enrichment: Optional per-image processing, sent as deep-object query params such as
              enrichment[resolution]=true.

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          max_age_ms: Reuse a cached result this many milliseconds old or newer. Default: 86400000 (1
              day). Set to 0 to bypass cache. Maximum: 2592000000 (30 days).

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              collecting images. Min: 0. Max: 30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "actions": actions,
                        "dedupe": dedupe,
                        "enrichment": enrichment,
                        "headers": headers,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "wait_for_ms": wait_for_ms,
                    },
                    brand_web_scrape_images_params.BrandWebScrapeImagesParams,
                ),
            ),
            cast_to=BrandWebScrapeImagesResponse,
        )

    def web_scrape_md(
        self,
        *,
        url: str,
        actions: Optional[Iterable[brand_web_scrape_md_params.Action]] | Omit = omit,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        exclude_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        include_frames: Union[bool, Literal["true", "false"]] | Omit = omit,
        include_images: Union[bool, Literal["true", "false"]] | Omit = omit,
        include_links: Union[bool, Literal["true", "false"]] | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        pdf: brand_web_scrape_md_params.Pdf | Omit = omit,
        settle_animations: Union[bool, Literal["true", "false"]] | Omit = omit,
        shorten_base64_images: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: Union[bool, Literal["true", "false"]] | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeMdResponse:
        """Scrapes the given URL into LLM usable Markdown.

        Inspect key_metadata on JSON
        responses from a recognized API key; use error_code to distinguish stable
        failure categories.

        ### Billing & errors

        | HTTP status | Billed?                                   | Meaning                                                                                  |
        | ----------- | ----------------------------------------- | ---------------------------------------------------------------------------------------- |
        | 200         | Yes — 1 credit, or 2 credits with actions | Successful scrape, including a zero-length result when includeSelectors matched nothing  |
        | 400         | No                                        | Invalid input, skipped PDF, or the page could not be scraped                             |
        | 401 / 403   | No                                        | Invalid/disabled key, insufficient permissions, or credits exhausted; inspect error_code |
        | 404         | No                                        | Target page returned or fingerprinted as not found                                       |
        | 408         | No                                        | Request timed out                                                                        |
        | 413         | No                                        | Target content exceeds the maximum supported size (20 MB)                                |
        | 415         | No                                        | Unsupported content type                                                                 |
        | 429         | No                                        | Per-minute rate limit exceeded; honor Retry-After                                        |
        | 500         | No                                        | Internal error                                                                           |

        Args:
          url: Full URL to scrape into LLM usable Markdown (must include http:// or https://
              protocol)

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove before conversion to Markdown. Applied after
              includeSelectors. Exclusion takes precedence: an element matching both is
              removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          include_frames: When true, the contents of iframes are rendered to Markdown.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          include_selectors: CSS selectors. When provided, only matching HTML subtrees (and their
              descendants) are kept before conversion to Markdown. When omitted, the entire
              document is kept. Examples: "article.main", "#content", "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              converting to Markdown. Defaults to false. This adds a bit of latency in
              exchange for more stable output on animated pages.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              converting the page to Markdown. Min: 0. Max: 30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "actions": actions,
                        "country": country,
                        "exclude_selectors": exclude_selectors,
                        "headers": headers,
                        "include_frames": include_frames,
                        "include_images": include_images,
                        "include_links": include_links,
                        "include_selectors": include_selectors,
                        "max_age_ms": max_age_ms,
                        "pdf": pdf,
                        "settle_animations": settle_animations,
                        "shorten_base64_images": shorten_base64_images,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
                    },
                    brand_web_scrape_md_params.BrandWebScrapeMdParams,
                ),
            ),
            cast_to=BrandWebScrapeMdResponse,
        )

    def web_scrape_sitemap(
        self,
        *,
        domain: str,
        headers: Dict[str, str] | Omit = omit,
        max_links: int | Omit = omit,
        search: str | Omit = omit,
        sitemap_url: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        url_regex: str | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeSitemapResponse:
        """Crawl an entire website's sitemap and return all discovered page URLs.

        Pass
        `search` to have the crawled sitemap filtered down to the pages about a phrase
        (for example `pricing and plans` or `api authentication docs`), most relevant
        first — a searched crawl scans the whole sitemap and costs 2 credits instead
        of 1.

        Args:
          domain: Domain to build a sitemap for

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

          search: Optional search phrase. When provided, the crawled sitemap is filtered to the
              pages whose URLs are about that phrase, most relevant first, and the request
              costs 2 credits instead of 1.

          sitemap_url: Optional explicit sitemap URL. When provided, exactly this sitemap is crawled
              instead of discovering the domain's sitemaps.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Optional RE2-compatible regex pattern. Only URLs matching this pattern are
              returned and counted against maxLinks.

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/sitemap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "headers": headers,
                        "max_links": max_links,
                        "search": search,
                        "sitemap_url": sitemap_url,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "url_regex": url_regex,
                        "zdr": zdr,
                    },
                    brand_web_scrape_sitemap_params.BrandWebScrapeSitemapParams,
                ),
            ),
            cast_to=BrandWebScrapeSitemapResponse,
        )


class AsyncBrandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/deprecated-brand-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/deprecated-brand-python-sdk#with_streaming_response
        """
        return AsyncBrandResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        domain: str | Omit = omit,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        name: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        ticker: str | Omit = omit,
        ticker_exchange: Literal[
            "AMEX",
            "AMS",
            "AQS",
            "ASX",
            "ATH",
            "BER",
            "BME",
            "BRU",
            "BSE",
            "BUD",
            "BUE",
            "BVC",
            "CBOE",
            "CNQ",
            "CPH",
            "DFM",
            "DOH",
            "DUB",
            "DUS",
            "DXE",
            "EGX",
            "FSX",
            "HAM",
            "HEL",
            "HKSE",
            "HOSE",
            "ICE",
            "IOB",
            "IST",
            "JKT",
            "JNB",
            "JPX",
            "KLS",
            "KOE",
            "KSC",
            "KUW",
            "LIS",
            "LSE",
            "MCX",
            "MEX",
            "MIL",
            "MUN",
            "NASDAQ",
            "NEO",
            "NSE",
            "NYSE",
            "NZE",
            "OSL",
            "OTC",
            "PAR",
            "PNK",
            "PRA",
            "RIS",
            "SAO",
            "SAU",
            "SES",
            "SET",
            "SGO",
            "SHH",
            "SHZ",
            "SIX",
            "STO",
            "STU",
            "TAI",
            "TAL",
            "TLV",
            "TSX",
            "TSXV",
            "TWO",
            "VIE",
            "WSE",
            "XETRA",
        ]
        | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """
        Retrieve logos, backdrops, colors, industry, description, and more from any
        domain

        Args:
          domain: Domain name to retrieve brand data for (e.g., 'example.com', 'google.com').
              Cannot be used with name or ticker parameters.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data. Works with all three lookup methods.

          name: Company name to retrieve brand data for (e.g., 'Apple Inc'). Cannot be used with
              domain or ticker parameters.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          ticker: Stock ticker symbol to retrieve brand data for (e.g., 'AAPL'). Cannot be used
              with domain or name parameters.

          ticker_exchange: Stock exchange code.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "name": name,
                        "tags": tags,
                        "ticker": ticker,
                        "ticker_exchange": ticker_exchange,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_params.BrandRetrieveParams,
                ),
            ),
            cast_to=BrandRetrieveResponse,
        )

    async def ai_product(
        self,
        *,
        url: str,
        max_age_ms: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductResponse:
        """
        Given a single URL, determines if it is a product page and extracts the product
        information.

        Args:
          url: The product page URL to extract product data from.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/ai/product",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "max_age_ms": max_age_ms,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                brand_ai_product_params.BrandAIProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIProductResponse,
        )

    @overload
    async def ai_products(
        self,
        *,
        domain: str,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        """Extract product information from a brand's website.

        We will analyze the website
        and return a list of products with details such as name, description, image,
        pricing, features, and more.

        Args:
          domain: The domain name to analyze.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_products: Maximum number of products to extract.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def ai_products(
        self,
        *,
        direct_url: str,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        """Extract product information from a brand's website.

        We will analyze the website
        and return a list of products with details such as name, description, image,
        pricing, features, and more.

        Args:
          direct_url: A specific URL to use directly as the starting point for extraction without
              domain resolution.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_products: Maximum number of products to extract.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["domain"], ["direct_url"])
    async def ai_products(
        self,
        *,
        domain: str | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        direct_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        return await self._post(
            "/brand/ai/products",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "max_age_ms": max_age_ms,
                    "max_products": max_products,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                    "direct_url": direct_url,
                },
                brand_ai_products_params.BrandAIProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIProductsResponse,
        )

    async def ai_query(
        self,
        *,
        data_to_extract: Iterable[brand_ai_query_params.DataToExtract],
        domain: str,
        specific_pages: brand_ai_query_params.SpecificPages | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIQueryResponse:
        """Use AI to extract specific data points from a brand's website.

        The AI will crawl
        the website and extract the requested information based on the provided data
        points.

        Args:
          data_to_extract: Array of data points to extract from the website

          domain: The domain name to analyze

          specific_pages: Optional object specifying which pages to analyze

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/ai/query",
            body=await async_maybe_transform(
                {
                    "data_to_extract": data_to_extract,
                    "domain": domain,
                    "specific_pages": specific_pages,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                brand_ai_query_params.BrandAIQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIQueryResponse,
        )

    async def fonts(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandFontsResponse:
        """
        Scrape font information from a website including font families, usage
        statistics, fallbacks, and element/word counts.

        Args:
          direct_url: A specific URL to fetch fonts from directly, bypassing domain resolution (e.g.,
              'https://example.com/design-system'). When provided, fonts are extracted from
              this exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to extract fonts from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/fonts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_fonts_params.BrandFontsParams,
                ),
            ),
            cast_to=BrandFontsResponse,
        )

    async def identify_from_transaction(
        self,
        *,
        transaction_info: str,
        city: str | Omit = omit,
        country_gl: Literal[
            "af",
            "al",
            "dz",
            "as",
            "ad",
            "ao",
            "ai",
            "aq",
            "ag",
            "ar",
            "am",
            "aw",
            "au",
            "at",
            "az",
            "bs",
            "bh",
            "bd",
            "bb",
            "by",
            "be",
            "bz",
            "bj",
            "bm",
            "bt",
            "bo",
            "ba",
            "bw",
            "bv",
            "br",
            "io",
            "bn",
            "bg",
            "bf",
            "bi",
            "kh",
            "cm",
            "ca",
            "cv",
            "ky",
            "cf",
            "td",
            "cl",
            "cn",
            "cx",
            "cc",
            "co",
            "km",
            "cg",
            "cd",
            "ck",
            "cr",
            "ci",
            "hr",
            "cu",
            "cy",
            "cz",
            "dk",
            "dj",
            "dm",
            "do",
            "ec",
            "eg",
            "sv",
            "gq",
            "er",
            "ee",
            "et",
            "fk",
            "fo",
            "fj",
            "fi",
            "fr",
            "gf",
            "pf",
            "tf",
            "ga",
            "gm",
            "ge",
            "de",
            "gh",
            "gi",
            "gr",
            "gl",
            "gd",
            "gp",
            "gu",
            "gt",
            "gn",
            "gw",
            "gy",
            "ht",
            "hm",
            "va",
            "hn",
            "hk",
            "hu",
            "is",
            "in",
            "id",
            "ir",
            "iq",
            "ie",
            "il",
            "it",
            "jm",
            "jp",
            "jo",
            "kz",
            "ke",
            "ki",
            "kp",
            "kr",
            "kw",
            "kg",
            "la",
            "lv",
            "lb",
            "ls",
            "lr",
            "ly",
            "li",
            "lt",
            "lu",
            "mo",
            "mk",
            "mg",
            "mw",
            "my",
            "mv",
            "ml",
            "mt",
            "mh",
            "mq",
            "mr",
            "mu",
            "yt",
            "mx",
            "fm",
            "md",
            "mc",
            "mn",
            "ms",
            "ma",
            "mz",
            "mm",
            "na",
            "nr",
            "np",
            "nl",
            "an",
            "nc",
            "nz",
            "ni",
            "ne",
            "ng",
            "nu",
            "nf",
            "mp",
            "no",
            "om",
            "pk",
            "pw",
            "ps",
            "pa",
            "pg",
            "py",
            "pe",
            "ph",
            "pn",
            "pl",
            "pt",
            "pr",
            "qa",
            "re",
            "ro",
            "ru",
            "rw",
            "sh",
            "kn",
            "lc",
            "pm",
            "vc",
            "ws",
            "sm",
            "st",
            "sa",
            "sn",
            "rs",
            "sc",
            "sl",
            "sg",
            "sk",
            "si",
            "sb",
            "so",
            "za",
            "gs",
            "es",
            "lk",
            "sd",
            "sr",
            "sj",
            "sz",
            "se",
            "ch",
            "sy",
            "tw",
            "tj",
            "tz",
            "th",
            "tl",
            "tg",
            "tk",
            "to",
            "tt",
            "tn",
            "tr",
            "tm",
            "tc",
            "tv",
            "ug",
            "ua",
            "ae",
            "gb",
            "us",
            "um",
            "uy",
            "uz",
            "vu",
            "ve",
            "vn",
            "vg",
            "vi",
            "wf",
            "eh",
            "ye",
            "zm",
            "zw",
        ]
        | Omit = omit,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        high_confidence_only: Union[bool, Literal["true", "false"]] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        mcc: Union[str, float] | Omit = omit,
        phone: Union[str, float] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandIdentifyFromTransactionResponse:
        """
        Endpoint specially designed for platforms that want to identify transaction data
        by the transaction title.

        Args:
          transaction_info: Transaction information to identify the brand

          city: Optional city name to prioritize when searching for the brand.

          country_gl: Two-letter ISO 3166-1 alpha-2 country code (GL parameter) used to localize
              search.

          force_language: Language to force for the retrieved brand data.

          high_confidence_only: When set to true, the API will perform an additional verification steps to
              ensure the identified brand matches the transaction with high confidence.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          mcc: Optional Merchant Category Code (MCC) to help identify the business
              category/industry.

          phone: Optional phone number from the transaction to help verify brand match.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/transaction_identifier",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "transaction_info": transaction_info,
                        "city": city,
                        "country_gl": country_gl,
                        "force_language": force_language,
                        "high_confidence_only": high_confidence_only,
                        "max_speed": max_speed,
                        "mcc": mcc,
                        "phone": phone,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_identify_from_transaction_params.BrandIdentifyFromTransactionParams,
                ),
            ),
            cast_to=BrandIdentifyFromTransactionResponse,
        )

    async def prefetch(
        self,
        *,
        domain: str,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandPrefetchResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency.

        Args:
          domain: Domain name to prefetch brand data for

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/prefetch",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                brand_prefetch_params.BrandPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchResponse,
        )

    async def prefetch_by_email(
        self,
        *,
        email: str,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandPrefetchByEmailResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency. This endpoint accepts an email address, extracts the domain from it,
        validates that it's not a disposable or free email provider, and queues the
        domain for prefetching.

        Args:
          email: Email address to prefetch brand data for. The domain will be extracted from the
              email. Free email providers (gmail.com, yahoo.com, etc.) and disposable email
              addresses are not allowed.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/prefetch-by-email",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                brand_prefetch_by_email_params.BrandPrefetchByEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchByEmailResponse,
        )

    async def retrieve_by_email(
        self,
        *,
        email: str,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByEmailResponse:
        """
        Retrieve brand information using an email address while detecting disposable and
        free email addresses. Disposable and free email addresses (like gmail.com,
        yahoo.com) will throw a 422 error.

        Args:
          email: Email address to retrieve brand data for (e.g., 'contact@example.com'). The
              domain will be extracted from the email. Free email providers (gmail.com,
              yahoo.com, etc.) and disposable email addresses are not allowed.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-by-email",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email": email,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_email_params.BrandRetrieveByEmailParams,
                ),
            ),
            cast_to=BrandRetrieveByEmailResponse,
        )

    async def retrieve_by_isin(
        self,
        *,
        isin: str,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByIsinResponse:
        """
        Retrieve brand information using an ISIN (International Securities
        Identification Number).

        Args:
          isin: ISIN (International Securities Identification Number) to retrieve brand data for
              (e.g., 'AU000000IMD5', 'US0378331005'). Must be exactly 12 characters: 2 letters
              followed by 9 alphanumeric characters and ending with a digit.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-by-isin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "isin": isin,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_isin_params.BrandRetrieveByIsinParams,
                ),
            ),
            cast_to=BrandRetrieveByIsinResponse,
        )

    async def retrieve_by_name(
        self,
        *,
        name: str,
        country_gl: Literal[
            "af",
            "al",
            "dz",
            "as",
            "ad",
            "ao",
            "ai",
            "aq",
            "ag",
            "ar",
            "am",
            "aw",
            "au",
            "at",
            "az",
            "bs",
            "bh",
            "bd",
            "bb",
            "by",
            "be",
            "bz",
            "bj",
            "bm",
            "bt",
            "bo",
            "ba",
            "bw",
            "bv",
            "br",
            "io",
            "bn",
            "bg",
            "bf",
            "bi",
            "kh",
            "cm",
            "ca",
            "cv",
            "ky",
            "cf",
            "td",
            "cl",
            "cn",
            "cx",
            "cc",
            "co",
            "km",
            "cg",
            "cd",
            "ck",
            "cr",
            "ci",
            "hr",
            "cu",
            "cy",
            "cz",
            "dk",
            "dj",
            "dm",
            "do",
            "ec",
            "eg",
            "sv",
            "gq",
            "er",
            "ee",
            "et",
            "fk",
            "fo",
            "fj",
            "fi",
            "fr",
            "gf",
            "pf",
            "tf",
            "ga",
            "gm",
            "ge",
            "de",
            "gh",
            "gi",
            "gr",
            "gl",
            "gd",
            "gp",
            "gu",
            "gt",
            "gn",
            "gw",
            "gy",
            "ht",
            "hm",
            "va",
            "hn",
            "hk",
            "hu",
            "is",
            "in",
            "id",
            "ir",
            "iq",
            "ie",
            "il",
            "it",
            "jm",
            "jp",
            "jo",
            "kz",
            "ke",
            "ki",
            "kp",
            "kr",
            "kw",
            "kg",
            "la",
            "lv",
            "lb",
            "ls",
            "lr",
            "ly",
            "li",
            "lt",
            "lu",
            "mo",
            "mk",
            "mg",
            "mw",
            "my",
            "mv",
            "ml",
            "mt",
            "mh",
            "mq",
            "mr",
            "mu",
            "yt",
            "mx",
            "fm",
            "md",
            "mc",
            "mn",
            "ms",
            "ma",
            "mz",
            "mm",
            "na",
            "nr",
            "np",
            "nl",
            "an",
            "nc",
            "nz",
            "ni",
            "ne",
            "ng",
            "nu",
            "nf",
            "mp",
            "no",
            "om",
            "pk",
            "pw",
            "ps",
            "pa",
            "pg",
            "py",
            "pe",
            "ph",
            "pn",
            "pl",
            "pt",
            "pr",
            "qa",
            "re",
            "ro",
            "ru",
            "rw",
            "sh",
            "kn",
            "lc",
            "pm",
            "vc",
            "ws",
            "sm",
            "st",
            "sa",
            "sn",
            "rs",
            "sc",
            "sl",
            "sg",
            "sk",
            "si",
            "sb",
            "so",
            "za",
            "gs",
            "es",
            "lk",
            "sd",
            "sr",
            "sj",
            "sz",
            "se",
            "ch",
            "sy",
            "tw",
            "tj",
            "tz",
            "th",
            "tl",
            "tg",
            "tk",
            "to",
            "tt",
            "tn",
            "tr",
            "tm",
            "tc",
            "tv",
            "ug",
            "ua",
            "ae",
            "gb",
            "us",
            "um",
            "uy",
            "uz",
            "vu",
            "ve",
            "vn",
            "vg",
            "vi",
            "wf",
            "eh",
            "ye",
            "zm",
            "zw",
        ]
        | Omit = omit,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByNameResponse:
        """
        Retrieve brand information using a company name.

        Args:
          name: Company name to retrieve brand data for (e.g., 'Apple Inc', 'Microsoft
              Corporation'). Must be 3-30 characters.

          country_gl: Two-letter ISO 3166-1 alpha-2 country code (GL parameter) used to localize
              search.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-by-name",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "country_gl": country_gl,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_name_params.BrandRetrieveByNameParams,
                ),
            ),
            cast_to=BrandRetrieveByNameResponse,
        )

    async def retrieve_by_ticker(
        self,
        *,
        ticker: str,
        force_language: Optional[
            Literal[
                "afrikaans",
                "albanian",
                "amharic",
                "arabic",
                "armenian",
                "assamese",
                "aymara",
                "azeri",
                "basque",
                "belarusian",
                "bengali",
                "bosnian",
                "bulgarian",
                "burmese",
                "cantonese",
                "catalan",
                "cebuano",
                "chinese",
                "corsican",
                "croatian",
                "czech",
                "danish",
                "dutch",
                "english",
                "esperanto",
                "estonian",
                "farsi",
                "fijian",
                "finnish",
                "french",
                "galician",
                "georgian",
                "german",
                "greek",
                "guarani",
                "gujarati",
                "haitian-creole",
                "hausa",
                "hawaiian",
                "hebrew",
                "hindi",
                "hmong",
                "hungarian",
                "icelandic",
                "igbo",
                "indonesian",
                "irish",
                "italian",
                "japanese",
                "javanese",
                "kannada",
                "kazakh",
                "khmer",
                "kinyarwanda",
                "korean",
                "kurdish",
                "kyrgyz",
                "lao",
                "latin",
                "latvian",
                "lingala",
                "lithuanian",
                "luxembourgish",
                "macedonian",
                "malagasy",
                "malay",
                "malayalam",
                "maltese",
                "maori",
                "marathi",
                "mongolian",
                "nepali",
                "norwegian",
                "odia",
                "oromo",
                "pashto",
                "pidgin",
                "polish",
                "portuguese",
                "punjabi",
                "quechua",
                "romanian",
                "russian",
                "samoan",
                "scottish-gaelic",
                "serbian",
                "sesotho",
                "shona",
                "sindhi",
                "sinhala",
                "slovak",
                "slovene",
                "somali",
                "spanish",
                "sundanese",
                "swahili",
                "swedish",
                "tagalog",
                "tajik",
                "tamil",
                "tatar",
                "telugu",
                "thai",
                "tibetan",
                "tigrinya",
                "tongan",
                "tswana",
                "turkish",
                "turkmen",
                "ukrainian",
                "urdu",
                "uyghur",
                "uzbek",
                "vietnamese",
                "welsh",
                "wolof",
                "xhosa",
                "yiddish",
                "yoruba",
                "zulu",
            ]
        ]
        | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_speed: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        ticker_exchange: Literal[
            "AMEX",
            "AMS",
            "AQS",
            "ASX",
            "ATH",
            "BER",
            "BME",
            "BRU",
            "BSE",
            "BUD",
            "BUE",
            "BVC",
            "CBOE",
            "CNQ",
            "CPH",
            "DFM",
            "DOH",
            "DUB",
            "DUS",
            "DXE",
            "EGX",
            "FSX",
            "HAM",
            "HEL",
            "HKSE",
            "HOSE",
            "ICE",
            "IOB",
            "IST",
            "JKT",
            "JNB",
            "JPX",
            "KLS",
            "KOE",
            "KSC",
            "KUW",
            "LIS",
            "LSE",
            "MCX",
            "MEX",
            "MIL",
            "MUN",
            "NASDAQ",
            "NEO",
            "NSE",
            "NYSE",
            "NZE",
            "OSL",
            "OTC",
            "PAR",
            "PNK",
            "PRA",
            "RIS",
            "SAO",
            "SAU",
            "SES",
            "SET",
            "SGO",
            "SHH",
            "SHZ",
            "SIX",
            "STO",
            "STU",
            "TAI",
            "TAL",
            "TLV",
            "TSX",
            "TSXV",
            "TWO",
            "VIE",
            "WSE",
            "XETRA",
        ]
        | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByTickerResponse:
        """
        Retrieve brand information using a stock ticker symbol.

        Args:
          ticker: Stock ticker symbol to retrieve brand data for (e.g., 'AAPL', 'GOOGL', 'BRK.A').
              Must be 1-15 characters, letters/numbers/dots only.

          force_language: Language to force for the retrieved brand data.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          ticker_exchange: Stock exchange code.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-by-ticker",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ticker": ticker,
                        "force_language": force_language,
                        "max_age_ms": max_age_ms,
                        "max_speed": max_speed,
                        "tags": tags,
                        "ticker_exchange": ticker_exchange,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_ticker_params.BrandRetrieveByTickerParams,
                ),
            ),
            cast_to=BrandRetrieveByTickerResponse,
        )

    async def retrieve_naics(
        self,
        *,
        input: str,
        max_results: int | Omit = omit,
        min_results: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveNaicsResponse:
        """
        Classify any brand into 2022 NAICS industry codes from its domain or name.

        Args:
          input: Brand domain or title to retrieve NAICS code for. If a valid domain is provided,
              it will be used for classification, otherwise, we will search for the brand
              using the provided title.

          max_results: Maximum number of NAICS codes to return. Must be between 1 and 10. Defaults
              to 5.

          min_results: Minimum number of NAICS codes to return. Must be at least 1. Defaults to 1.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/naics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "input": input,
                        "max_results": max_results,
                        "min_results": min_results,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_naics_params.BrandRetrieveNaicsParams,
                ),
            ),
            cast_to=BrandRetrieveNaicsResponse,
        )

    async def retrieve_simplified(
        self,
        *,
        domain: str,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        theme: Literal["light", "dark"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveSimplifiedResponse:
        """
        Returns a simplified version of brand data containing only essential
        information: domain, title, colors, logos, and backdrops. Optimized for faster
        responses and reduced data transfer.

        Args:
          domain: Domain name to retrieve simplified brand data for

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          theme: Optional theme preference used when selecting brand assets.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-simplified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "theme": theme,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_simplified_params.BrandRetrieveSimplifiedParams,
                ),
            ),
            cast_to=BrandRetrieveSimplifiedResponse,
        )

    async def screenshot(
        self,
        *,
        color_scheme: Literal["light", "dark"] | Omit = omit,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        handle_cookie_popup: Union[bool, Literal["true", "false"]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        scroll_offset: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        viewport: brand_screenshot_params.Viewport | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandScreenshotResponse:
        """
        Capture a screenshot of a website.

        Args:
          color_scheme: Optional parameter to choose the site's visual theme in the screenshot. Use
              'light' or 'dark' when the site offers both appearances.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          handle_cookie_popup: Optional parameter to control cookie/consent popup handling. If 'true', we
              dismiss cookie banner before capture. If 'false' or not provided, captures the
              page without that step.

          max_age_ms: Return a cached screenshot if a prior screenshot for the same parameters exists
              and is younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always capture fresh.

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          scroll_offset: Optional vertical scroll offset in pixels for capturing a long page in
              viewport-sized chunks. When provided, the full page is captured once and the
              returned image is the viewport-sized slice that begins at this Y offset (e.g.
              request scrollOffset=0, then 1080, then 2160 to walk a 1920x1080 landing page
              top to bottom). The final slice may be shorter than the viewport height. Takes
              precedence over fullScreenshot. Max: 100000.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          viewport: Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080.

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before taking
              the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
              omitted.

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "color_scheme": color_scheme,
                        "country": country,
                        "direct_url": direct_url,
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "handle_cookie_popup": handle_cookie_popup,
                        "max_age_ms": max_age_ms,
                        "page": page,
                        "scroll_offset": scroll_offset,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "viewport": viewport,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
                    },
                    brand_screenshot_params.BrandScreenshotParams,
                ),
            ),
            cast_to=BrandScreenshotResponse,
        )

    async def styleguide(
        self,
        *,
        color_scheme: Literal["light", "dark"] | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandStyleguideResponse:
        """
        Extract a comprehensive design system from a website including colors,
        typography, spacing, shadows, and UI components.

        Args:
          color_scheme: Optional browser color scheme to emulate for websites that respond to
              prefers-color-scheme. This value is part of the styleguide cache key.

          direct_url: A specific URL to fetch the styleguide from directly, bypassing domain
              resolution (e.g., 'https://example.com/design-system'). When provided, the
              styleguide is extracted from this exact URL. You must provide either 'domain' or
              'directUrl', but not both.

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/styleguide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "color_scheme": color_scheme,
                        "direct_url": direct_url,
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                    },
                    brand_styleguide_params.BrandStyleguideParams,
                ),
            ),
            cast_to=BrandStyleguideResponse,
        )

    async def web_scrape_html(
        self,
        *,
        url: str,
        actions: Optional[Iterable[brand_web_scrape_html_params.Action]] | Omit = omit,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        exclude_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        include_frames: Union[bool, Literal["true", "false"]] | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        pdf: brand_web_scrape_html_params.Pdf | Omit = omit,
        settle_animations: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: Union[bool, Literal["true", "false"]] | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeHTMLResponse:
        """Scrapes the given URL and returns the raw HTML content of the page.

        The base
        request costs 1 credit; requests with browser actions cost 2 credits.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove from the result. Applied after includeSelectors.
              Exclusion takes precedence: an element matching both is removed. Examples:
              "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          include_frames: When true, iframes are rendered inline into the returned HTML.

          include_selectors: CSS selectors. When provided, only matching subtrees (and their descendants) are
              kept and everything else is dropped. When omitted, the entire document is kept.
              Examples: "article.main", "#content", "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              extracting HTML. Defaults to false. This adds a bit of latency in exchange for
              more stable output on animated pages.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: When true, return only the page's main content in the HTML response, excluding
              headers, footers, sidebars, and navigation when detectable.

          wait_for_ms:
              Optional browser wait time in milliseconds after initial page load. Min: 0. Max:
              30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "actions": actions,
                        "country": country,
                        "exclude_selectors": exclude_selectors,
                        "headers": headers,
                        "include_frames": include_frames,
                        "include_selectors": include_selectors,
                        "max_age_ms": max_age_ms,
                        "pdf": pdf,
                        "settle_animations": settle_animations,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
                    },
                    brand_web_scrape_html_params.BrandWebScrapeHTMLParams,
                ),
            ),
            cast_to=BrandWebScrapeHTMLResponse,
        )

    async def web_scrape_images(
        self,
        *,
        url: str,
        actions: Optional[Iterable[brand_web_scrape_images_params.Action]] | Omit = omit,
        dedupe: Union[bool, Literal["true", "false"]] | Omit = omit,
        enrichment: Optional[brand_web_scrape_images_params.Enrichment] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeImagesResponse:
        """
        Extract image assets from a web page, including standard URLs, inline SVGs, data
        URIs, responsive image sources, metadata, CSS backgrounds, video posters, and
        embeds. The base request costs 1 credit, or 2 credits with browser actions. When
        enrichment is enabled, the entire call costs 5 credits, including requests that
        also use actions.

        Args:
          url: Page URL to inspect. Must include http:// or https://.

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          dedupe: When true, visually duplicate images are removed: every image is loaded and
              perceptually hashed, and only the highest-resolution copy of each duplicate
              group is kept. Images that cannot be downloaded or hashed are kept. Default:
              false.

          enrichment: Optional per-image processing, sent as deep-object query params such as
              enrichment[resolution]=true.

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          max_age_ms: Reuse a cached result this many milliseconds old or newer. Default: 86400000 (1
              day). Set to 0 to bypass cache. Maximum: 2592000000 (30 days).

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              collecting images. Min: 0. Max: 30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "actions": actions,
                        "dedupe": dedupe,
                        "enrichment": enrichment,
                        "headers": headers,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "wait_for_ms": wait_for_ms,
                    },
                    brand_web_scrape_images_params.BrandWebScrapeImagesParams,
                ),
            ),
            cast_to=BrandWebScrapeImagesResponse,
        )

    async def web_scrape_md(
        self,
        *,
        url: str,
        actions: Optional[Iterable[brand_web_scrape_md_params.Action]] | Omit = omit,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        exclude_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        include_frames: Union[bool, Literal["true", "false"]] | Omit = omit,
        include_images: Union[bool, Literal["true", "false"]] | Omit = omit,
        include_links: Union[bool, Literal["true", "false"]] | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        pdf: brand_web_scrape_md_params.Pdf | Omit = omit,
        settle_animations: Union[bool, Literal["true", "false"]] | Omit = omit,
        shorten_base64_images: Union[bool, Literal["true", "false"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: Union[bool, Literal["true", "false"]] | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeMdResponse:
        """Scrapes the given URL into LLM usable Markdown.

        Inspect key_metadata on JSON
        responses from a recognized API key; use error_code to distinguish stable
        failure categories.

        ### Billing & errors

        | HTTP status | Billed?                                   | Meaning                                                                                  |
        | ----------- | ----------------------------------------- | ---------------------------------------------------------------------------------------- |
        | 200         | Yes — 1 credit, or 2 credits with actions | Successful scrape, including a zero-length result when includeSelectors matched nothing  |
        | 400         | No                                        | Invalid input, skipped PDF, or the page could not be scraped                             |
        | 401 / 403   | No                                        | Invalid/disabled key, insufficient permissions, or credits exhausted; inspect error_code |
        | 404         | No                                        | Target page returned or fingerprinted as not found                                       |
        | 408         | No                                        | Request timed out                                                                        |
        | 413         | No                                        | Target content exceeds the maximum supported size (20 MB)                                |
        | 415         | No                                        | Unsupported content type                                                                 |
        | 429         | No                                        | Per-minute rate limit exceeded; honor Retry-After                                        |
        | 500         | No                                        | Internal error                                                                           |

        Args:
          url: Full URL to scrape into LLM usable Markdown (must include http:// or https://
              protocol)

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove before conversion to Markdown. Applied after
              includeSelectors. Exclusion takes precedence: an element matching both is
              removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          include_frames: When true, the contents of iframes are rendered to Markdown.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          include_selectors: CSS selectors. When provided, only matching HTML subtrees (and their
              descendants) are kept before conversion to Markdown. When omitted, the entire
              document is kept. Examples: "article.main", "#content", "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              converting to Markdown. Defaults to false. This adds a bit of latency in
              exchange for more stable output on animated pages.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              converting the page to Markdown. Min: 0. Max: 30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "actions": actions,
                        "country": country,
                        "exclude_selectors": exclude_selectors,
                        "headers": headers,
                        "include_frames": include_frames,
                        "include_images": include_images,
                        "include_links": include_links,
                        "include_selectors": include_selectors,
                        "max_age_ms": max_age_ms,
                        "pdf": pdf,
                        "settle_animations": settle_animations,
                        "shorten_base64_images": shorten_base64_images,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
                    },
                    brand_web_scrape_md_params.BrandWebScrapeMdParams,
                ),
            ),
            cast_to=BrandWebScrapeMdResponse,
        )

    async def web_scrape_sitemap(
        self,
        *,
        domain: str,
        headers: Dict[str, str] | Omit = omit,
        max_links: int | Omit = omit,
        search: str | Omit = omit,
        sitemap_url: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        url_regex: str | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeSitemapResponse:
        """Crawl an entire website's sitemap and return all discovered page URLs.

        Pass
        `search` to have the crawled sitemap filtered down to the pages about a phrase
        (for example `pricing and plans` or `api authentication docs`), most relevant
        first — a searched crawl scans the whole sitemap and costs 2 credits instead
        of 1.

        Args:
          domain: Domain to build a sitemap for

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

          search: Optional search phrase. When provided, the crawled sitemap is filtered to the
              pages whose URLs are about that phrase, most relevant first, and the request
              costs 2 credits instead of 1.

          sitemap_url: Optional explicit sitemap URL. When provided, exactly this sitemap is crawled
              instead of discovering the domain's sitemaps.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Optional RE2-compatible regex pattern. Only URLs matching this pattern are
              returned and counted against maxLinks.

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/sitemap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "headers": headers,
                        "max_links": max_links,
                        "search": search,
                        "sitemap_url": sitemap_url,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "url_regex": url_regex,
                        "zdr": zdr,
                    },
                    brand_web_scrape_sitemap_params.BrandWebScrapeSitemapParams,
                ),
            ),
            cast_to=BrandWebScrapeSitemapResponse,
        )


class BrandResourceWithRawResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_raw_response_wrapper(
            brand.retrieve,
        )
        self.ai_product = to_raw_response_wrapper(
            brand.ai_product,
        )
        self.ai_products = to_raw_response_wrapper(
            brand.ai_products,
        )
        self.ai_query = to_raw_response_wrapper(
            brand.ai_query,
        )
        self.fonts = to_raw_response_wrapper(
            brand.fonts,
        )
        self.identify_from_transaction = to_raw_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = to_raw_response_wrapper(
            brand.prefetch,
        )
        self.prefetch_by_email = to_raw_response_wrapper(
            brand.prefetch_by_email,
        )
        self.retrieve_by_email = to_raw_response_wrapper(
            brand.retrieve_by_email,
        )
        self.retrieve_by_isin = to_raw_response_wrapper(
            brand.retrieve_by_isin,
        )
        self.retrieve_by_name = to_raw_response_wrapper(
            brand.retrieve_by_name,
        )
        self.retrieve_by_ticker = to_raw_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_naics = to_raw_response_wrapper(
            brand.retrieve_naics,
        )
        self.retrieve_simplified = to_raw_response_wrapper(
            brand.retrieve_simplified,
        )
        self.screenshot = to_raw_response_wrapper(
            brand.screenshot,
        )
        self.styleguide = to_raw_response_wrapper(
            brand.styleguide,
        )
        self.web_scrape_html = to_raw_response_wrapper(
            brand.web_scrape_html,
        )
        self.web_scrape_images = to_raw_response_wrapper(
            brand.web_scrape_images,
        )
        self.web_scrape_md = to_raw_response_wrapper(
            brand.web_scrape_md,
        )
        self.web_scrape_sitemap = to_raw_response_wrapper(
            brand.web_scrape_sitemap,
        )


class AsyncBrandResourceWithRawResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_raw_response_wrapper(
            brand.retrieve,
        )
        self.ai_product = async_to_raw_response_wrapper(
            brand.ai_product,
        )
        self.ai_products = async_to_raw_response_wrapper(
            brand.ai_products,
        )
        self.ai_query = async_to_raw_response_wrapper(
            brand.ai_query,
        )
        self.fonts = async_to_raw_response_wrapper(
            brand.fonts,
        )
        self.identify_from_transaction = async_to_raw_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = async_to_raw_response_wrapper(
            brand.prefetch,
        )
        self.prefetch_by_email = async_to_raw_response_wrapper(
            brand.prefetch_by_email,
        )
        self.retrieve_by_email = async_to_raw_response_wrapper(
            brand.retrieve_by_email,
        )
        self.retrieve_by_isin = async_to_raw_response_wrapper(
            brand.retrieve_by_isin,
        )
        self.retrieve_by_name = async_to_raw_response_wrapper(
            brand.retrieve_by_name,
        )
        self.retrieve_by_ticker = async_to_raw_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_naics = async_to_raw_response_wrapper(
            brand.retrieve_naics,
        )
        self.retrieve_simplified = async_to_raw_response_wrapper(
            brand.retrieve_simplified,
        )
        self.screenshot = async_to_raw_response_wrapper(
            brand.screenshot,
        )
        self.styleguide = async_to_raw_response_wrapper(
            brand.styleguide,
        )
        self.web_scrape_html = async_to_raw_response_wrapper(
            brand.web_scrape_html,
        )
        self.web_scrape_images = async_to_raw_response_wrapper(
            brand.web_scrape_images,
        )
        self.web_scrape_md = async_to_raw_response_wrapper(
            brand.web_scrape_md,
        )
        self.web_scrape_sitemap = async_to_raw_response_wrapper(
            brand.web_scrape_sitemap,
        )


class BrandResourceWithStreamingResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.ai_product = to_streamed_response_wrapper(
            brand.ai_product,
        )
        self.ai_products = to_streamed_response_wrapper(
            brand.ai_products,
        )
        self.ai_query = to_streamed_response_wrapper(
            brand.ai_query,
        )
        self.fonts = to_streamed_response_wrapper(
            brand.fonts,
        )
        self.identify_from_transaction = to_streamed_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = to_streamed_response_wrapper(
            brand.prefetch,
        )
        self.prefetch_by_email = to_streamed_response_wrapper(
            brand.prefetch_by_email,
        )
        self.retrieve_by_email = to_streamed_response_wrapper(
            brand.retrieve_by_email,
        )
        self.retrieve_by_isin = to_streamed_response_wrapper(
            brand.retrieve_by_isin,
        )
        self.retrieve_by_name = to_streamed_response_wrapper(
            brand.retrieve_by_name,
        )
        self.retrieve_by_ticker = to_streamed_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_naics = to_streamed_response_wrapper(
            brand.retrieve_naics,
        )
        self.retrieve_simplified = to_streamed_response_wrapper(
            brand.retrieve_simplified,
        )
        self.screenshot = to_streamed_response_wrapper(
            brand.screenshot,
        )
        self.styleguide = to_streamed_response_wrapper(
            brand.styleguide,
        )
        self.web_scrape_html = to_streamed_response_wrapper(
            brand.web_scrape_html,
        )
        self.web_scrape_images = to_streamed_response_wrapper(
            brand.web_scrape_images,
        )
        self.web_scrape_md = to_streamed_response_wrapper(
            brand.web_scrape_md,
        )
        self.web_scrape_sitemap = to_streamed_response_wrapper(
            brand.web_scrape_sitemap,
        )


class AsyncBrandResourceWithStreamingResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.ai_product = async_to_streamed_response_wrapper(
            brand.ai_product,
        )
        self.ai_products = async_to_streamed_response_wrapper(
            brand.ai_products,
        )
        self.ai_query = async_to_streamed_response_wrapper(
            brand.ai_query,
        )
        self.fonts = async_to_streamed_response_wrapper(
            brand.fonts,
        )
        self.identify_from_transaction = async_to_streamed_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = async_to_streamed_response_wrapper(
            brand.prefetch,
        )
        self.prefetch_by_email = async_to_streamed_response_wrapper(
            brand.prefetch_by_email,
        )
        self.retrieve_by_email = async_to_streamed_response_wrapper(
            brand.retrieve_by_email,
        )
        self.retrieve_by_isin = async_to_streamed_response_wrapper(
            brand.retrieve_by_isin,
        )
        self.retrieve_by_name = async_to_streamed_response_wrapper(
            brand.retrieve_by_name,
        )
        self.retrieve_by_ticker = async_to_streamed_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_naics = async_to_streamed_response_wrapper(
            brand.retrieve_naics,
        )
        self.retrieve_simplified = async_to_streamed_response_wrapper(
            brand.retrieve_simplified,
        )
        self.screenshot = async_to_streamed_response_wrapper(
            brand.screenshot,
        )
        self.styleguide = async_to_streamed_response_wrapper(
            brand.styleguide,
        )
        self.web_scrape_html = async_to_streamed_response_wrapper(
            brand.web_scrape_html,
        )
        self.web_scrape_images = async_to_streamed_response_wrapper(
            brand.web_scrape_images,
        )
        self.web_scrape_md = async_to_streamed_response_wrapper(
            brand.web_scrape_md,
        )
        self.web_scrape_sitemap = async_to_streamed_response_wrapper(
            brand.web_scrape_sitemap,
        )
