USE_CLICK_OUTSIDE_TS = """
import { RefObject, useEffect } from 'react';

type ClickOutsideHandler = (event: MouseEvent | TouchEvent) => void;

export const useClickOutside = <T extends HTMLElement>(
  ref: RefObject<T>,
  handler: ClickOutsideHandler
): void => {
  useEffect(() => {
    const listener = (event: MouseEvent | TouchEvent) => {
      if (!ref.current || ref.current.contains(event.target as Node)) {
        return;
      }
      handler(event);
    };

    document.addEventListener('mousedown', listener);
    document.addEventListener('touchstart', listener);

    return () => {
      document.removeEventListener('mousedown', listener);
      document.removeEventListener('touchstart', listener);
    };
  }, [ref, handler]);
};
"""

