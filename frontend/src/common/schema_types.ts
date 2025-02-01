/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

export type SearchSettings = SearchSettings;

export interface ExploreSearch {
  query: string | null;
  cardTypes: ("CARD" | "CARDBACK" | "TOKEN")[];
  searchSettings: SearchSettings;
  pageStart: number;
  pageSize: number;
}
/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

export interface SearchQuery {
  query: string | null;
  card_type: "CARD" | "CARDBACK" | "TOKEN";
}
/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

/**
 * @minItems 2
 * @maxItems 2
 */
export type SourceRow = [number, boolean];

export interface SearchSettings {
  searchTypeSettings: SearchTypeSettings;
  sourceSettings: SourceSettings;
  filterSettings: FilterSettings;
}
export interface SearchTypeSettings {
  /**
   * Whether fuzzy search is enabled
   */
  fuzzySearch: boolean;
  /**
   * Whether search settings apply to cardbacks or not
   */
  filterCardbacks: boolean;
}
export interface SourceSettings {
  /**
   * The list of sources in the order they should be searched
   */
  sources: SourceRow[] | null;
}
export interface FilterSettings {
  /**
   * The minimum DPI that cards must meet to be included in search results
   */
  minimumDPI: number;
  /**
   * The maximum DPI that cards can have to be included in search results
   */
  maximumDPI: number;
  /**
   * The maximum filesize that cards can have to be included in search results
   */
  maximumSize: number;
  /**
   * The language the cards have to be written in to be included in search results
   */
  languages: string[];
  /**
   * The tags which the cards must have to be included in search results
   */
  includesTags: string[];
  /**
   * The tags which the cards must *not* have to be included in search results
   */
  excludesTags: string[];
}
